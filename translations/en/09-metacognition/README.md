<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-30T13:00:33+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "en"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.en.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Click the image above to view the video of this lesson)_
# Metacognition in AI Agents

## Introduction

Welcome to the lesson on metacognition in AI agents! This chapter is designed for beginners curious about how AI agents can reflect on their own thought processes. By the end of this lesson, you'll grasp key concepts and have practical examples to apply metacognition in designing AI agents.

## Learning Goals

After completing this lesson, you will be able to:

1. Understand the implications of reasoning loops in agent definitions.
2. Use planning and evaluation techniques to help agents self-correct.
3. Create agents capable of manipulating code to achieve tasks.

## Introduction to Metacognition

Metacognition refers to higher-order cognitive processes that involve thinking about one’s own thinking. For AI agents, this means being able to evaluate and adjust their actions based on self-awareness and past experiences. Metacognition, or "thinking about thinking," is a key concept in developing agentic AI systems. It involves AI systems being aware of their internal processes and being able to monitor, regulate, and adapt their behavior accordingly. Much like humans do when assessing a situation or solving a problem. This self-awareness can help AI systems make better decisions, identify errors, and improve their performance over time—again tying back to the Turing test and the debate over whether AI will surpass human intelligence.

In the context of agentic AI systems, metacognition can help address several challenges, such as:
- Transparency: Ensuring AI systems can explain their reasoning and decisions.
- Reasoning: Enhancing AI systems' ability to synthesize information and make sound decisions.
- Adaptation: Allowing AI systems to adjust to new environments and changing conditions.
- Perception: Improving AI systems' accuracy in recognizing and interpreting data from their environment.

### What is Metacognition?

Metacognition, or "thinking about thinking," is a higher-order cognitive process involving self-awareness and self-regulation of one’s cognitive processes. In AI, metacognition enables agents to evaluate and adapt their strategies and actions, leading to better problem-solving and decision-making. By understanding metacognition, you can design AI agents that are not only smarter but also more adaptable and efficient. True metacognition involves the AI explicitly reasoning about its own reasoning.

Example: “I prioritized cheaper flights because… I might be missing out on direct flights, so let me re-check.”
Tracking how or why it chose a certain route:
- Noting that it made mistakes by over-relying on user preferences from last time, so it modifies its decision-making strategy, not just the final recommendation.
- Diagnosing patterns like, “Whenever I see the user mention ‘too crowded,’ I should not only remove certain attractions but also rethink my method of ranking ‘top attractions’ if I always prioritize popularity.”

### Importance of Metacognition in AI Agents

Metacognition is crucial in AI agent design for several reasons:

![Importance of Metacognition](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.en.png)

- Self-Reflection: Agents can assess their own performance and identify areas for improvement.
- Adaptability: Agents can modify their strategies based on past experiences and changing environments.
- Error Correction: Agents can detect and correct errors autonomously, leading to more accurate outcomes.
- Resource Management: Agents can optimize resources like time and computational power by planning and evaluating their actions.

## Components of an AI Agent

Before diving into metacognitive processes, it’s essential to understand the basic components of an AI agent. An AI agent typically consists of:

- Persona: The personality and characteristics of the agent, which define how it interacts with users.
- Tools: The capabilities and functions the agent can perform.
- Skills: The knowledge and expertise the agent possesses.

These components work together to create an "expertise unit" capable of performing specific tasks.

**Example**:
Consider a travel agent service that not only plans your holiday but also adjusts its recommendations based on real-time data and past customer experiences.

### Example: Metacognition in a Travel Agent Service

Imagine you’re designing a travel agent service powered by AI. This agent, "Travel Agent," helps users plan their vacations. To incorporate metacognition, Travel Agent needs to evaluate and adjust its actions based on self-awareness and past experiences. Here’s how metacognition could play a role:

#### Current Task

The current task is to help a user plan a trip to Paris.

#### Steps to Complete the Task

1. **Gather User Preferences**: Ask the user about their travel dates, budget, interests (e.g., museums, cuisine, shopping), and any specific requirements.
2. **Retrieve Information**: Search for flight options, accommodations, attractions, and restaurants that match the user’s preferences.
3. **Generate Recommendations**: Provide a personalized itinerary with flight details, hotel reservations, and suggested activities.
4. **Adjust Based on Feedback**: Ask the user for feedback on the recommendations and make necessary adjustments.

#### Required Resources

- Access to flight and hotel booking databases.
- Information on Parisian attractions and restaurants.
- User feedback data from previous interactions.

#### Experience and Self-Reflection

Travel Agent uses metacognition to evaluate its performance and learn from past experiences. For example:

1. **Analyzing User Feedback**: Travel Agent reviews user feedback to determine which recommendations were well-received and which were not. It adjusts its future suggestions accordingly.
2. **Adaptability**: If a user has previously mentioned a dislike for crowded places, Travel Agent will avoid recommending popular tourist spots during peak hours in the future.
3. **Error Correction**: If Travel Agent made an error in a past booking, such as suggesting a hotel that was fully booked, it learns to check availability more rigorously before making recommendations.

#### Practical Developer Example

Here’s a simplified example of how Travel Agent’s code might look when incorporating metacognition:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Why Metacognition Matters

- **Self-Reflection**: Agents can analyze their performance and identify areas for improvement.
- **Adaptability**: Agents can modify strategies based on feedback and changing conditions.
- **Error Correction**: Agents can autonomously detect and correct mistakes.
- **Resource Management**: Agents can optimize resource usage, such as time and computational power.

By incorporating metacognition, Travel Agent can provide more personalized and accurate travel recommendations, enhancing the overall user experience.

---

## 2. Planning in Agents

Planning is a critical component of AI agent behavior. It involves outlining the steps needed to achieve a goal, considering the current state, resources, and possible obstacles.

### Elements of Planning

- **Current Task**: Define the task clearly.
- **Steps to Complete the Task**: Break down the task into manageable steps.
- **Required Resources**: Identify necessary resources.
- **Experience**: Utilize past experiences to inform planning.

**Example**:
Here are the steps Travel Agent needs to take to assist a user in planning their trip effectively:

### Steps for Travel Agent

1. **Gather User Preferences**
   - Ask the user for details about their travel dates, budget, interests, and any specific requirements.
   - Examples: "When are you planning to travel?" "What is your budget range?" "What activities do you enjoy on vacation?"

2. **Retrieve Information**
   - Search for relevant travel options based on user preferences.
   - **Flights**: Look for available flights within the user’s budget and preferred travel dates.
   - **Accommodations**: Find hotels or rental properties that match the user’s preferences for location, price, and amenities.
   - **Attractions and Restaurants**: Identify popular attractions, activities, and dining options that align with the user’s interests.

3. **Generate Recommendations**
   - Compile the retrieved information into a personalized itinerary.
   - Provide details such as flight options, hotel reservations, and suggested activities, making sure to tailor the recommendations to the user’s preferences.

4. **Present Itinerary to User**
   - Share the proposed itinerary with the user for their review.
   - Example: "Here’s a suggested itinerary for your trip to Paris. It includes flight details, hotel bookings, and a list of recommended activities and restaurants. Let me know your thoughts!"

5. **Collect Feedback**
   - Ask the user for feedback on the proposed itinerary.
   - Examples: "Do you like the flight options?" "Is the hotel suitable for your needs?" "Are there any activities you would like to add or remove?"

6. **Adjust Based on Feedback**
   - Modify the itinerary based on the user’s feedback.
   - Make necessary changes to flight, accommodation, and activity recommendations to better match the user’s preferences.

7. **Final Confirmation**
   - Present the updated itinerary to the user for final confirmation.
   - Example: "I’ve made the adjustments based on your feedback. Here’s the updated itinerary. Does everything look good to you?"

8. **Book and Confirm Reservations**
   - Once the user approves the itinerary, proceed with booking flights, accommodations, and any pre-planned activities.
   - Send confirmation details to the user.

9. **Provide Ongoing Support**
   - Remain available to assist the user with any changes or additional requests before and during their trip.
   - Example: "If you need any further assistance during your trip, feel free to reach out to me anytime!"

### Example Interaction

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Corrective RAG System

First, let’s understand the difference between RAG Tool and Pre-emptive Context Load.

![RAG vs Context Loading](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.en.png)

### Retrieval-Augmented Generation (RAG)

RAG combines a retrieval system with a generative model. When a query is made, the retrieval system fetches relevant documents or data from an external source, and this retrieved information is used to augment the input to the generative model. This helps the model generate more accurate and contextually relevant responses.

In a RAG system, the agent retrieves relevant information from a knowledge base and uses it to generate appropriate responses or actions.

### Corrective RAG Approach

The Corrective RAG approach focuses on using RAG techniques to correct errors and improve the accuracy of AI agents. This involves:

1. **Prompting Technique**: Using specific prompts to guide the agent in retrieving relevant information.
2. **Tool**: Implementing algorithms and mechanisms that enable the agent to evaluate the relevance of the retrieved information and generate accurate responses.
3. **Evaluation**: Continuously assessing the agent’s performance and making adjustments to improve its accuracy and efficiency.

#### Example: Corrective RAG in a Search Agent

Consider a search agent that retrieves information from the web to answer user queries. The Corrective RAG approach might involve:

1. **Prompting Technique**: Formulating search queries based on the user’s input.
2. **Tool**: Using natural language processing and machine learning algorithms to rank and filter search results.
3. **Evaluation**: Analyzing user feedback to identify and correct inaccuracies in the retrieved information.

### Corrective RAG in Travel Agent

Corrective RAG (Retrieval-Augmented Generation) enhances an AI’s ability to retrieve and generate information while correcting any inaccuracies. Let’s see how Travel Agent can use the Corrective RAG approach to provide more accurate and relevant travel recommendations.

This involves:

- **Prompting Technique**: Using specific prompts to guide the agent in retrieving relevant information.
- **Tool**: Implementing algorithms and mechanisms that enable the agent to evaluate the relevance of the retrieved information and generate accurate responses.
- **Evaluation**: Continuously assessing the agent’s performance and making adjustments to improve its accuracy and efficiency.

#### Steps for Implementing Corrective RAG in Travel Agent

1. **Initial User Interaction**
   - Travel Agent gathers initial preferences from the user, such as destination, travel dates, budget, and interests.
   - Example:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Retrieval of Information**
   - Travel Agent retrieves information about flights, accommodations, attractions, and restaurants based on user preferences.
   - Example:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generating Initial Recommendations**
   - Travel Agent uses the retrieved information to generate a personalized itinerary.
   - Example:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Collecting User Feedback**
   - Travel Agent asks the user for feedback on the initial recommendations.
   - Example:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Corrective RAG Process**
   - **Prompting Technique**: Travel Agent formulates new search queries based on user feedback.
     - Example:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Tool**: Travel Agent uses algorithms to rank and filter new search results, emphasizing the relevance based on user feedback.
     - Example:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluation**: Travel Agent continuously assesses the relevance and accuracy of its recommendations by analyzing user feedback and making necessary adjustments.
     - Example:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Practical Example

Here’s a simplified Python code example incorporating the Corrective RAG approach in Travel Agent:
### Pre-emptive Context Load

Pre-emptive Context Load involves preparing relevant background information for the model before it processes a query. This ensures the model has access to this data from the beginning, enabling it to provide more accurate responses without needing to fetch additional information during the process.

Here's a simple example of how pre-emptive context load might work for a travel agent application in Python:

#### Explanation

1. **Initialization (`__init__` method)**: The `TravelAgent` class loads a dictionary with details about popular destinations like Paris, Tokyo, New York, and Sydney. This dictionary includes information such as the country, currency, language, and major attractions for each destination.

2. **Retrieving Information (`get_destination_info` method)**: When a user asks about a specific destination, the `get_destination_info` method retrieves the relevant details from the pre-loaded dictionary.

By pre-loading the context, the travel agent application can quickly respond to user queries without needing to fetch this information from external sources in real-time, making the application faster and more efficient.

### Bootstrapping the Plan with a Goal Before Iterating

Bootstrapping a plan with a goal means starting with a clear objective or desired outcome. Defining this goal upfront helps guide the model throughout the iterative process, ensuring each step moves closer to achieving the target efficiently and effectively.

#### Scenario

A travel agent wants to create a personalized vacation plan for a client. The goal is to design an itinerary that maximizes the client's satisfaction based on their preferences and budget.

#### Steps

1. Identify the client's preferences and budget.
2. Create an initial plan based on these preferences.
3. Refine the plan through iterations, optimizing for the client's satisfaction.

#### Code Explanation

1. **Initialization (`__init__` method)**: The `TravelAgent` class initializes with a list of destinations, each with attributes like name, cost, and activity type.

2. **Bootstrapping the Plan (`bootstrap_plan` method)**: This method generates an initial travel plan by selecting destinations that match the client's preferences and fit within their budget.

3. **Matching Preferences (`match_preferences` method)**: This method checks whether a destination aligns with the client's preferences.

4. **Iterating the Plan (`iterate_plan` method)**: This method refines the initial plan by attempting to replace destinations with better options that still meet the client's preferences and budget.

5. **Calculating Cost (`calculate_cost` method)**: This method calculates the total cost of the current plan, including potential new destinations.

#### Example Usage

- **Initial Plan**: The travel agent creates a plan based on the client's preference for sightseeing and a budget of $2000.
- **Refined Plan**: The travel agent iterates the plan to better align with the client's preferences and budget.

By starting with a clear goal (e.g., maximizing client satisfaction) and refining the plan iteratively, the travel agent can create a tailored and optimized travel itinerary for the client.

### Taking Advantage of LLM for Re-ranking and Scoring

Large Language Models (LLMs) can be used to re-rank and score retrieved documents or generated responses based on their relevance and quality. Here's how this process works:

**Retrieval:** The initial step fetches a set of candidate documents or responses based on the query.

**Re-ranking:** The LLM evaluates these candidates and re-orders them based on their relevance and quality, ensuring the most useful information appears first.

**Scoring:** The LLM assigns scores to each candidate, reflecting their relevance and quality. This helps select the best response or document for the user.

Using LLMs for re-ranking and scoring improves the accuracy and contextual relevance of the information provided, enhancing the user experience.

#### Scenario - Travel Based on Preferences

A travel agent wants to recommend the best travel destinations to a client based on their preferences. The LLM will re-rank and score the destinations to ensure the most relevant options are presented.

#### Steps:

1. Gather user preferences.
2. Retrieve a list of potential travel destinations.
3. Use the LLM to re-rank and score the destinations based on user preferences.

#### Code Explanation - Preference Booker

1. **Initialization**: The `TravelAgent` class initializes with a list of destinations, each with attributes like name and description.

2. **Getting Recommendations (`get_recommendations` method)**: This method generates a prompt for the Azure OpenAI service based on the user's preferences and sends an HTTP POST request to the Azure OpenAI API to get re-ranked and scored destinations.

3. **Generating Prompt (`generate_prompt` method)**: This method creates a prompt for Azure OpenAI, including the user's preferences and the list of destinations. The prompt guides the model to re-rank and score the destinations.

4. **API Call**: The `requests` library sends an HTTP POST request to the Azure OpenAI API endpoint. The response contains the re-ranked and scored destinations.

5. **Example Usage**: The travel agent collects user preferences (e.g., interest in sightseeing and diverse culture) and uses Azure OpenAI to get personalized recommendations.

By using LLMs for re-ranking and scoring, the travel agent can offer more tailored and relevant travel suggestions, improving the overall client experience.

### RAG: Prompting Technique vs Tool

Retrieval-Augmented Generation (RAG) can function as both a prompting technique and a tool. Understanding the difference helps in effectively applying RAG in projects.

#### RAG as a Prompting Technique

**What is it?**

- RAG as a prompting technique involves crafting specific queries or prompts to retrieve relevant information from a database or corpus. This information is then used to generate responses.

**How it works:**

1. **Formulate Prompts**: Create structured prompts based on the user's input or task requirements.
2. **Retrieve Information**: Use the prompts to search for relevant data in a knowledge base.
3. **Generate Response**: Combine the retrieved data with generative AI models to produce a coherent response.

**Example in Travel Agent**:

- User Input: "I want to visit museums in Paris."
- Prompt: "Find top museums in Paris."
- Retrieved Information: Details about Louvre Museum, Musée d'Orsay, etc.
- Generated Response: "Here are some top museums in Paris: Louvre Museum, Musée d'Orsay, and Centre Pompidou."

#### RAG as a Tool

**What is it?**

- RAG as a tool is an integrated system that automates the retrieval and generation process, simplifying complex AI functionalities without requiring manual prompts for each query.

**How it works:**

1. **Integration**: Embed RAG into the AI agent's architecture to handle retrieval and generation tasks automatically.
2. **Automation**: The tool manages the process from user input to response generation without explicit prompts.
3. **Efficiency**: Streamlines the process for faster and more accurate responses.

**Example in Travel Agent**:

- User Input: "I want to visit museums in Paris."
- RAG Tool: Automatically retrieves information about museums and generates a response.
- Generated Response: "Here are some top museums in Paris: Louvre Museum, Musée d'Orsay, and Centre Pompidou."

### Comparison

| Aspect                 | Prompting Technique                                        | Tool                                                  |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| **Manual vs Automatic**| Manual formulation of prompts for each query.               | Automated process for retrieval and generation.       |
| **Control**            | Offers more control over the retrieval process.             | Streamlines and automates the retrieval and generation.|
| **Flexibility**        | Allows for customized prompts based on specific needs.      | More efficient for large-scale implementations.       |
| **Complexity**         | Requires crafting and tweaking of prompts.                  | Easier to integrate within an AI agent's architecture. |

### Evaluating Relevancy

Evaluating relevancy ensures the information retrieved and generated by the AI agent is accurate, appropriate, and useful to the user.

#### Key Concepts in Evaluating Relevancy

1. **Context Awareness**:
   - The agent must understand the user's query context to provide relevant information.
   - Example: If a user asks for "best restaurants in Paris," the agent should consider preferences like cuisine type and budget.

2. **Accuracy**:
   - Information should be factually correct and up-to-date.
   - Example: Recommending currently open restaurants with good reviews.

3. **User Intent**:
   - The agent should infer the user's intent to provide the most relevant information.
   - Example: If a user asks for "budget-friendly hotels," prioritize affordable options.

4. **Feedback Loop**:
   - Collecting and analyzing user feedback helps refine relevancy evaluation.
   - Example: Using user ratings to improve future recommendations.

#### Practical Techniques for Evaluating Relevancy

1. **Relevance Scoring**:
   - Assign scores to items based on how well they match the user's query and preferences.

2. **Filtering and Ranking**:
   - Filter irrelevant items and rank the rest based on relevance scores.

3. **Natural Language Processing (NLP)**:
   - Use NLP to understand the user's query and retrieve relevant information.

4. **User Feedback Integration**:
   - Incorporate user feedback to adjust future relevance evaluations.

#### Example: Evaluating Relevancy in Travel Agent

A travel agent evaluates the relevancy of travel recommendations by scoring destinations based on user preferences and refining the list accordingly.

### Search with Intent

Searching with intent focuses on understanding the user's underlying purpose or goal to retrieve and generate the most relevant information.

#### Key Concepts in Searching with Intent

1. **Understanding User Intent**:
   - Categorize intent into informational, navigational, and transactional types.
     - **Informational Intent**: Seeking knowledge (e.g., "What are the best museums in Paris?").
     - **Navigational Intent**: Looking for a specific site (e.g., "Louvre Museum official website").
     - **Transactional Intent**: Aiming to complete a task (e.g., "Book a flight to Paris").

2. **Context Awareness**:
   - Analyze the query's context, including user preferences and previous interactions.

3. **Natural Language Processing (NLP)**:
   - Use NLP to interpret natural language queries, including entity recognition and sentiment analysis.

4. **Personalization**:
   - Tailor search results based on user history and preferences for enhanced relevancy.
#### Practical Example: Searching with Intent in Travel Agent

Let's use Travel Agent as an example to understand how intent-based searching can be implemented.

1. **Collecting User Preferences**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Interpreting User Intent**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Being Context-Aware**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Searching and Personalizing Results**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Example Usage**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Generating Code as a Tool

Code-generating agents utilize AI models to write and execute code, enabling them to solve complex problems and automate tasks.

### Code-Generating Agents

These agents leverage generative AI models to write and execute code. They can tackle complex challenges, automate workflows, and provide valuable insights by generating and running code in various programming languages.

#### Practical Applications

1. **Automated Code Generation**: Create code snippets for tasks like data analysis, web scraping, or machine learning.
2. **SQL as a RAG**: Use SQL queries to retrieve and manipulate data from databases.
3. **Problem Solving**: Write and execute code to address specific challenges, such as optimizing algorithms or analyzing datasets.

#### Example: Code-Generating Agent for Data Analysis

Imagine designing a code-generating agent. Here's how it might function:

1. **Task**: Analyze a dataset to uncover trends and patterns.
2. **Steps**:
   - Load the dataset into a data analysis tool.
   - Generate SQL queries to filter and aggregate the data.
   - Execute the queries and retrieve the results.
   - Use the results to create visualizations and insights.
3. **Required Resources**: Access to the dataset, data analysis tools, and SQL capabilities.
4. **Experience**: Leverage past analysis results to enhance the accuracy and relevance of future analyses.

### Example: Code-Generating Agent for Travel Agent

In this example, we'll design a code-generating agent, Travel Agent, to help users plan their trips by generating and executing code. This agent can perform tasks like retrieving travel options, filtering results, and creating an itinerary using generative AI.

#### Overview of the Code-Generating Agent

1. **Collecting User Preferences**: Gathers user input such as destination, travel dates, budget, and interests.
2. **Generating Code to Fetch Data**: Creates code snippets to retrieve information about flights, hotels, and attractions.
3. **Executing Generated Code**: Runs the generated code to obtain real-time data.
4. **Creating an Itinerary**: Compiles the retrieved data into a personalized travel plan.
5. **Refining Based on Feedback**: Accepts user feedback and regenerates code as needed to improve results.

#### Step-by-Step Implementation

1. **Collecting User Preferences**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generating Code to Fetch Data**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Executing Generated Code**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Creating an Itinerary**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Refining Based on Feedback**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Leveraging Environmental Awareness and Reasoning

Incorporating table schema awareness can enhance query generation by utilizing environmental context and reasoning.

Here's an example of how this can be achieved:

1. **Understanding the Schema**: The system interprets the table schema and uses this knowledge to guide query generation.
2. **Adapting Based on Feedback**: The system adjusts user preferences based on feedback and determines which schema fields need updates.
3. **Generating and Executing Queries**: The system creates and runs queries to fetch updated flight and hotel data based on revised preferences.

Below is an updated Python code example that demonstrates these concepts:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Explanation - Booking Based on Feedback

1. **Schema Awareness**: The `schema` dictionary defines how preferences should be modified based on feedback, including fields like `favorites` and `avoid` with corresponding adjustments.
2. **Adjusting Preferences (`adjust_based_on_feedback` method)**: This method modifies preferences based on user feedback and the schema.
3. **Environment-Based Adjustments (`adjust_based_on_environment` method)**: This method tailors adjustments using the schema and feedback.
4. **Generating and Executing Queries**: The system generates code to fetch updated flight and hotel data based on the adjusted preferences and simulates query execution.
5. **Creating an Itinerary**: The system generates an updated itinerary using the new flight, hotel, and attraction data.

By making the system aware of its environment and reasoning based on the schema, it can produce more accurate and relevant queries, resulting in better travel recommendations and a more personalized user experience.

### Using SQL as a Retrieval-Augmented Generation (RAG) Technique

SQL (Structured Query Language) is a robust tool for interacting with databases. When integrated into a Retrieval-Augmented Generation (RAG) approach, SQL can retrieve relevant data from databases to inform and generate responses or actions in AI agents. Let's explore how SQL can be applied as a RAG technique in the context of Travel Agent.

#### Key Concepts

1. **Database Interaction**:
   - SQL is used to query databases, retrieve relevant information, and manipulate data.
   - Example: Fetching flight details, hotel options, and attractions from a travel database.

2. **Integration with RAG**:
   - SQL queries are generated based on user input and preferences.
   - The retrieved data is used to create personalized recommendations or actions.

3. **Dynamic Query Generation**:
   - The AI agent dynamically generates SQL queries based on the context and user needs.
   - Example: Customizing SQL queries to filter results by budget, dates, and interests.

#### Applications

- **Automated Code Generation**: Create code snippets for specific tasks.
- **SQL as a RAG**: Use SQL queries to manipulate data.
- **Problem Solving**: Write and execute code to address challenges.

**Example**:
A data analysis agent:

1. **Task**: Analyze a dataset to identify trends.
2. **Steps**:
   - Load the dataset.
   - Generate SQL queries to filter data.
   - Execute queries and retrieve results.
   - Create visualizations and insights.
3. **Resources**: Dataset access, SQL capabilities.
4. **Experience**: Use past results to improve future analyses.

#### Practical Example: Using SQL in Travel Agent

1. **Collecting User Preferences**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generating SQL Queries**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Executing SQL Queries**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Creating Recommendations**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Example SQL Queries

1. **Flight Query**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotel Query**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Attraction Query**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

By incorporating SQL into the Retrieval-Augmented Generation (RAG) technique, AI agents like Travel Agent can dynamically retrieve and utilize relevant data to deliver accurate and personalized recommendations.

### Example of Metacognition

To demonstrate metacognition, let's create a simple agent that *reflects on its decision-making process* while solving a problem. In this example, the agent will optimize hotel selection but evaluate its reasoning and adjust its strategy when it makes errors or suboptimal choices.

#### How this illustrates metacognition:

1. **Initial Decision**: The agent selects the cheapest hotel without considering quality.
2. **Reflection and Evaluation**: After the initial choice, the agent evaluates whether the hotel was a poor choice based on user feedback. If the quality is too low, it reflects on its reasoning.
3. **Adjusting Strategy**: The agent modifies its strategy, switching from "cheapest" to "highest_quality," improving its decision-making process for future iterations.

Here's an example:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agent's Metacognitive Abilities

The agent demonstrates the ability to:
- Evaluate its previous decisions and reasoning process.
- Adjust its strategy based on reflection, showcasing metacognition in action.

This is a basic example of metacognition, where the system refines its reasoning process based on internal feedback.

### Conclusion

Metacognition is a powerful concept that can significantly enhance AI agents' capabilities. By incorporating metacognitive processes, you can design agents that are more intelligent, adaptable, and efficient. Explore additional resources to dive deeper into the fascinating world of metacognition in AI agents.

### Got More Questions about the Metacognition Design Pattern?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agents questions answered.

## Previous Lesson

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Next Lesson

[AI Agents in Production](../10-ai-agents-production/README.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.