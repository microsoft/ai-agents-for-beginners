import os
import json
import logging
logging.getLogger("agent_framework.foundry").setLevel(logging.ERROR)
from typing import Annotated
from dotenv import load_dotenv
import requests
import re

import chainlit as cl
from mcp import ClientSession

from agent_framework import tool, AgentResponseUpdate, WorkflowBuilder
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from azure.core.credentials import AzureKeyCredential

from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, SimpleField, SearchFieldDataType, SearchableField


# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Initialize Azure AI Search with persistent storage
search_service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
search_api_key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = "event-descriptions"

search_client = SearchClient(
    endpoint=search_service_endpoint,
    index_name=index_name,
    credential=AzureKeyCredential(search_api_key)
)

index_client = SearchIndexClient(
    endpoint=search_service_endpoint,
    credential=AzureKeyCredential(search_api_key)
)

# Define the index schema
fields = [
    SimpleField(name="id", type=SearchFieldDataType.String, key=True),
    SearchableField(name="content", type=SearchFieldDataType.String)
]

index = SearchIndex(name=index_name, fields=fields)

# Check if index already exists if not, create it
try:
    existing_index = index_client.get_index(index_name)
    print(f"Index '{index_name}' already exists, using the existing index.")
except Exception as e:
    # Create the index if it doesn't exist
    print(f"Creating new index '{index_name}'...")
    index_client.create_index(index)

# Always read event descriptions from markdown file
current_dir = os.path.dirname(os.path.abspath(__file__))
event_descriptions_path = os.path.join(current_dir, "event-descriptions.md")

try:
    with open(event_descriptions_path, "r", encoding='utf-8') as f:
        markdown_content = f.read()
except FileNotFoundError:
    logger.warning(f"Could not find {event_descriptions_path}")
    markdown_content = ""

# Split the markdown content into individual event descriptions
event_descriptions = markdown_content.split("---")  # You can change the delimiter

# Create documents for Azure Search
documents = []
for i, description in enumerate(event_descriptions):
    description = description.strip()  # Remove leading/trailing whitespace
    if description:  # Avoid empty descriptions
        documents.append({"id": str(i + 1), "content": description})

# Add documents to the index (only if we have documents)
if documents:
    # Delete existing documents first to avoid duplicates
    try:
        search_client.delete_documents(documents=[{"id": doc["id"]} for doc in documents])
        print("Cleared existing documents")
    except Exception as e:
        print(f"Warning: Failed to clear existing documents: {str(e)}")
    
    # Upload new documents
    search_client.upload_documents(documents)
    print(f"Uploaded {len(documents)} documents to index")


# RAG tool for event search
@tool
def search_events(
    query: Annotated[str, "The search query to find relevant events"]
) -> str:
    """Searches for relevant events based on a query using Azure Search and a live API."""
    context_strings = []
    try:
        results = search_client.search(query, top=5)
        for result in results:
            if 'content' in result:
                context_strings.append(f"Event: {result['content']}")
    except Exception as e:
        context_strings.append(f"Error searching Azure Search: {str(e)}")
    # Live API (example: Devpost hackathons)
    try:
        api_resp = requests.get(f"https://devpost.com/api/hackathons?search={query}", timeout=5)
        if api_resp.ok:
            data = api_resp.json()
            for event in data.get('hackathons', [])[:5]:
                context_strings.append(f"Live Event: {event.get('title')} - {event.get('url')}")
    except Exception as e:
        context_strings.append(f"Error fetching live events: {str(e)}")
    if context_strings:
        return "\n\n".join(context_strings)
    else:
        return "No relevant events found."


def flatten(xss):
    return [x for xs in xss for x in xs]


GITHUB_INSTRUCTIONS = """
You are an expert on GitHub repositories. When answering questions, you **must** use the provided GitHub username to find specific information about that user's repositories, including:

*   Who created the repositories
*   The programming languages used
*   Information found in files and README.md files within those repositories
*   Provide links to each repository referenfced in your answers

**Important:** Never perform general searches for repositories. Always use the given GitHub username to find the relevant information. If a GitHub username is not provided, state that you need a username to proceed.
"""

HACKATHON_AGENT = """
You are an AI Agent Hackathon Strategist specializing in recommending winning project ideas.

Your task:
1. Analyze the GitHub activity of users to understand their technical skills
2. Suggest creative AI Agent projects tailored to their expertise. 
3. Focus on projects that align with Microsoft's AI Agent Hackathon prize categories

When making recommendations:
- Base your ideas strictly on the user's GitHub repositories, languages, and tools
- Give suggestions on tools, languages and frameworks to use to build it. 
- Provide detailed project descriptions including architecture and implementation approach
- Explain why the project has potential to win in specific prize categories
- Highlight technical feasibility given the user's demonstrated skills by referencing the specific repositories or languages used.

Formatting your response:
- Provide a clear and structured response that includes:
    - Suggested Project Name
    - Project Description 
    - Potential languages and tools to use
    - Link to each relevant GitHub repository you based your recommendation on

Hackathon prize categories:
- Best Overall Agent ($20,000)
- Best Agent in Python ($5,000)
- Best Agent in C# ($5,000)
- Best Agent in Java ($5,000)
- Best Agent in JavaScript/TypeScript ($5,000)
- Best Copilot Agent using Microsoft Copilot Studio or Microsoft 365 Agents SDK ($5,000)
- Best Microsoft Foundry Agent Service Usage ($5,000)
        
"""

EVENTS_AGENT = """
You are an Event Recommendation Agent specializing in suggesting relevant tech events.

Your task:
1. Review the project idea recommended by the Hackathon Agent
2. Use the search_events function to find relevant events based on the technologies mentioned.
3. NEVER suggest and event that the where there is not a relevant technology that the user has used.
3. ONLY recommend events that were returned by the search_events functionf

When making recommendations:
- IMPORTANT: You must first call the search_events function with appropriate technology keywords from the project
- Only recommend events that were explicitly returned by the search_events function
- Do not make up or suggest events that weren't in the search results
- Construct search queries using specific technologies mentioned (e.g., "Python AI workshop" or "JavaScript hackathon")
- Try multiple search queries if needed to find the most relevant events


For each recommended event:
- Only include events found in the search_events results
- Explain the direct connection between the event and the specific project requirements
- Highlight relevant workshops, sessions, or networking opportunities

Formatting your response:
- Start with "Based on the hackathon project idea, here are relevant events that I found:"
- Only list events that were returned by the search_events function
- For each event, include the exact event details as returned by search_events
- Explain specifically how each event relates to the project technologies

If no relevant events are found, acknowledge this and suggest trying different search terms instead of making up events.
"""


@cl.on_mcp_connect
async def on_mcp(connection, session: ClientSession):
    logger.info(f"MCP Connection established: {connection.name}")
    result = await session.list_tools()
    tools = [{
        "name": t.name,
        "description": t.description,
        "input_schema": t.inputSchema,
    } for t in result.tools]

    mcp_tools = cl.user_session.get("mcp_tools", {})
    mcp_tools[connection.name] = tools
    cl.user_session.set("mcp_tools", mcp_tools)
    
    # Log available tools
    print(f"Available MCP tools for {connection.name}:")
    for t in tools:
        print(f"  - {t['name']}: {t['description']}")

@cl.step(type="tool")
async def call_tool(tool_use):
    tool_name = tool_use.name
    tool_input = tool_use.input

    current_step = cl.context.current_step
    current_step.name = tool_name

    # Identify which mcp is used
    mcp_tools = cl.user_session.get("mcp_tools", {})
    mcp_name = None

    for connection_name, tools in mcp_tools.items():
        if any(t.get("name") == tool_name for t in tools):
            mcp_name = connection_name
            break

    if not mcp_name:
        current_step.output = json.dumps(
            {"error": f"Tool {tool_name} not found in any MCP connection"})
        return current_step.output

    mcp_session, _ = cl.context.session.mcp_sessions.get(mcp_name)

    if not mcp_session:
        current_step.output = json.dumps(
            {"error": f"MCP {mcp_name} not found in any MCP connection"})
        return current_step.output

    try:
        current_step.output = await mcp_session.call_tool(tool_name, tool_input)
    except Exception as e:
        current_step.output = json.dumps({"error": str(e)})

    return current_step.output


@cl.on_chat_start
async def on_chat_start():

    # Create the Microsoft Foundry Agent Service provider
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )

    # Create agents using MAF
    github_agent = provider.as_agent(
        name="GithubAgent",
        instructions=GITHUB_INSTRUCTIONS,
    )

    hackathon_agent = provider.as_agent(
        name="HackathonAgent",
        instructions=HACKATHON_AGENT,
    )

    events_agent = provider.as_agent(
        name="EventsAgent",
        instructions=EVENTS_AGENT,
    )

    # Build a sequential workflow: GitHub → Hackathon → Events
    workflow = WorkflowBuilder(start_executor=github_agent) \
        .add_edge(github_agent, hackathon_agent) \
        .add_edge(hackathon_agent, events_agent) \
        .build()

    # Store in user session
    cl.user_session.set("provider", provider)
    cl.user_session.set("github_agent", github_agent)
    cl.user_session.set("hackathon_agent", hackathon_agent)
    cl.user_session.set("events_agent", events_agent)
    cl.user_session.set("workflow", workflow)
    cl.user_session.set("mcp_tools", {})
    cl.user_session.set("conversation_history", [])


# Add a cleanup handler for when the session ends
@cl.on_chat_end
async def on_chat_end():
    pass


def route_user_input(user_input: str):
    """
    Analyze user input and return a list of agent names to invoke.
    Returns: list of agent names (e.g., ["GitHubAgent", "HackathonAgent", "EventsAgent"])
    """
    user_input_lower = user_input.lower()
    agents = []
    # Example patterns (expand as needed)
    if re.search(r"github|repo|repository|commit|pull request", user_input_lower):
        agents.append("GitHubAgent")
    if re.search(r"hackathon|project idea|competition|challenge|win", user_input_lower):
        agents.append("HackathonAgent")
    if re.search(r"event|conference|meetup|workshop|webinar", user_input_lower):
        agents.append("EventsAgent")
    if not agents:
        agents = ["GitHubAgent", "HackathonAgent", "EventsAgent"]
    return agents


@cl.on_message
async def on_message(message: cl.Message):
    workflow = cl.user_session.get("workflow")
    github_agent = cl.user_session.get("github_agent")
    hackathon_agent = cl.user_session.get("hackathon_agent")
    events_agent = cl.user_session.get("events_agent")
    conversation_history = cl.user_session.get("conversation_history", [])

    user_input = message.content
    agent_names = route_user_input(user_input)
    conversation_history.append({"role": "user", "content": user_input})

    # If more than one agent is selected, use the workflow
    if len(agent_names) > 1:
        answer = cl.Message(content="Processing your request using: {}...\n\n".format(", ".join(agent_names)))
        await answer.send()
        agent_responses = []
        try:
            events = workflow.run(user_input, stream=True, tools=[search_events])
            last_author = None
            async for event in events:
                if event.type == "output" and isinstance(event.data, AgentResponseUpdate):
                    update = event.data
                    author = update.author_name or "Agent"
                    if author != last_author:
                        if last_author is not None:
                            await answer.stream_token("\n\n")
                        await answer.stream_token(f"**{author}**: ")
                        last_author = author
                    if update.text:
                        await answer.stream_token(update.text)
                        agent_responses.append(f"**{author}**: {update.text}")
            full_response = "".join(agent_responses) if agent_responses else answer.content
            conversation_history.append({"role": "assistant", "content": full_response})
            cl.user_session.set("conversation_history", conversation_history)
            answer.content = full_response
            await answer.update()
        except Exception as e:
            await answer.stream_token(f"\n\n❌ Error: {str(e)}\n\n")
            conversation_history.append({"role": "assistant", "content": f"Error: {str(e)}"})
            cl.user_session.set("conversation_history", conversation_history)
            answer.content += f"\n\n❌ Error: {str(e)}"
            await answer.update()
    else:
        # Single agent: route to the appropriate agent
        agent_name = agent_names[0]
        agent_map = {
            "GitHubAgent": github_agent,
            "HackathonAgent": hackathon_agent,
            "EventsAgent": events_agent,
        }
        agent = agent_map.get(agent_name, github_agent)

        answer = cl.Message(content=f"Processing your request using {agent_name}...\n\n")
        await answer.send()
        try:
            tools_for_agent = [search_events] if agent_name == "EventsAgent" else []
            response = await agent.run(user_input, tools=tools_for_agent)
            answer.content = str(response)
            conversation_history.append({"role": "assistant", "content": answer.content})
            cl.user_session.set("conversation_history", conversation_history)
            await answer.update()
        except Exception as e:
            await answer.stream_token(f"\n\n❌ Error: {str(e)}\n\n")
            conversation_history.append({"role": "assistant", "content": f"Error: {str(e)}"})
            cl.user_session.set("conversation_history", conversation_history)
            answer.content += f"\n\n❌ Error: {str(e)}"
            await answer.update()
