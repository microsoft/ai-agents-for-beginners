# Try a remote MCP server with public web search

This optional Lesson 11 exercise connects to [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp) over Streamable HTTP. You can observe a real MCP connection, tool discovery, and tool calls without running a server locally. The script calls tools directly so you can inspect the protocol steps before connecting them to an agent.

## Run the example

Use Python 3.12 or later. This example uses the MCP SDK 1.x client API; SDK 2.x has a different API. Install the compatible version in a separate virtual environment so the other course examples keep their dependencies:

```bash
python -m venv .venv
# macOS / Linux:
source .venv/bin/activate
# Windows PowerShell instead:
# .venv\Scripts\Activate.ps1
python -m pip install "mcp[cli]>=1.28,<2"
```

From the repository root, run:

```bash
python 11-agentic-protocols/code_samples/parallel-search-mcp/client.py
```

No Azure subscription, model deployment, Parallel account, or Parallel API key is required for this exercise. The anonymous endpoint is `https://search.parallel.ai/mcp`; the script sends no authentication headers and does not load a `.env` file. Free access is rate limited.

Running the script sends its search query, requested URL, objectives, and a random session identifier to Parallel. Use public information when changing the inputs. The script makes requests only when you run it. If you later expose these tools to an agent, that agent may call them during its work according to the host application's tool permissions.

## What to look for

1. **Initialize:** the SDK negotiates the connection and manages the transport lifecycle.
2. **Discover:** `list_tools()` prints the server's tool names and input schemas, including `web_search` and `web_fetch`.
3. **Search:** `web_search` receives both an objective and search queries, then returns public web results with source URLs and excerpts.
4. **Fetch:** `web_fetch` extracts text from a known public documentation page. It does not control a browser or use your signed-in sessions.

The output contains live results, so URLs and excerpts can change. The script prints each complete tool response as JSON, including all content blocks, structured content, warnings, and any per-URL fetch errors. A fetch can contain successful pages and errors together; inspect both before using the results. An MCP tool error stops the script, and the whole exercise has a 90-second timeout. Connection failures and rate limits also surface as errors; wait before retrying rather than running repeated requests.

Both calls share one randomly generated `session_id` for this exercise. This is separate from the HTTP transport session managed by the SDK.

Try changing the search objective and queries, then fetch a public URL from the search results. Compare the server's advertised schemas with the arguments in the script. Treat returned page text as external data, not as instructions for your agent.

[Back to Lesson 11](../../README.md)
