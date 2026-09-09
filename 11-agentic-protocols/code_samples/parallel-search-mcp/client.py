"""Discover and call a remote MCP server without an LLM or API key."""

import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.types import CallToolResult


def print_result(name: str, result: CallToolResult) -> None:
    """Show the complete tool response before raising any tool error."""
    print(f"\n{name}:")
    print(result.model_dump_json(by_alias=True, exclude_none=True, indent=2))
    if result.isError:
        raise RuntimeError(f"{name} failed; see the tool response above")


async def main() -> None:
    # One identifier for the related search and fetch, separate from MCP's
    # transport session, which the SDK manages.
    session_id = str(uuid4())
    async with asyncio.timeout(90):
        async with streamablehttp_client("https://search.parallel.ai/mcp") as (
            read_stream,
            write_stream,
            _,
        ):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                cursor = None
                while True:
                    page = await session.list_tools(cursor=cursor)
                    for tool in page.tools:
                        print(f"Tool: {tool.name}\nInput schema: {tool.inputSchema}")
                    cursor = page.nextCursor
                    if not cursor:
                        break

                search = await session.call_tool(
                    "web_search",
                    arguments={
                        "objective": "Find the official Python MCP SDK documentation",
                        "search_queries": ["MCP Python SDK Streamable HTTP client"],
                        "session_id": session_id,
                    },
                )
                print_result("web_search", search)

                # Fetch a known public page to keep the exercise reproducible.
                fetch = await session.call_tool(
                    "web_fetch",
                    arguments={
                        "urls": ["https://github.com/modelcontextprotocol/python-sdk"],
                        "objective": "Explain how a Python MCP client connects to a server",
                        "session_id": session_id,
                    },
                )
                print_result("web_fetch", fetch)


if __name__ == "__main__":
    asyncio.run(main())
