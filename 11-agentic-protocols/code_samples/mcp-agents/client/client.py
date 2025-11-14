#!/usr/bin/env python3
"""
Interactive MCP Client for Agent-to-Agent Communication Tutorial
"""

import asyncio
import argparse
import logging
from typing import Dict, Any

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.server.streamable_http import MCP_SESSION_ID_HEADER, MCP_PROTOCOL_VERSION_HEADER
from mcp.shared.message import ClientMessageMetadata
import mcp.types as types
from rich.console import Console
from rich.panel import Panel

from .utils import TokenManager, cast_input_value

console = Console()


def display_tools(tools):
    """Display available tools as a simple list."""
    console.print("[bold]Available Tools:[/bold]")
    for tool in tools:
        tool_type = "🤖" if any(word in tool.name.lower() for word in ["agent", "travel", "research"]) else "🔧"
        console.print(f"  {tool_type} [cyan]{tool.name}[/cyan]")
    console.print()
    console.print("[dim]Type a tool name to run it with default arguments[/dim]")


def extract_text_content(result) -> str:
    """Extract text content from tool result."""
    for content in result.content:
        if hasattr(content, 'text'):
            return content.text
    return "No text content available"


async def execute_tool_with_resumption(session, command: str, args: dict, get_session_id, on_resumption_token_update, existing_tokens=None, token_manager=None):
    """Execute a tool with resumption support using send_request."""
    current_session_id = get_session_id()
    if not current_session_id:
        raise RuntimeError("No session ID available - resumption requires a valid session")
    
    session_id = current_session_id
    
    # If we have an existing resumption token, pass it for resumption
    if existing_tokens and existing_tokens.get("resumption_token"):
        metadata = ClientMessageMetadata(
            resumption_token=existing_tokens["resumption_token"],
        )
    else:
        # Create enhanced callback that saves tool context immediately when token is received
        def enhanced_callback(token: str):
            # Since callback fires immediately with the actual resumption token,
            # save everything needed for resumption right away
            protocol_version = getattr(session, 'protocol_version', None)
            if token_manager:
                token_manager.save_tokens(session_id, token, protocol_version, command, args)
            # Also call the original callback
            return on_resumption_token_update(session_id, token, command, args)
        
        metadata = ClientMessageMetadata(
            on_resumption_token_update=enhanced_callback,
        )
    
    result = await session.send_request(
        types.ClientRequest(
            types.CallToolRequest(
                method="tools/call",
                params=types.CallToolRequestParams(
                    name=command,
                    arguments=args
                ),
            )
        ),
        types.CallToolResult,
        metadata=metadata,
    )
    
    return result


async def interactive_mode(server_url: str):
    """Run interactive mode with tool exploration."""
    # Configure logging to suppress noisy SSE parsing errors
    logging.getLogger('mcp.client.streamable_http').setLevel(logging.ERROR)
    
    # Filter out specific SSE JSON parsing errors
    class SSEFilter(logging.Filter):
        def filter(self, record):
            # Suppress "Error parsing SSE message" and JSON validation errors
            if ("Error parsing SSE message" in record.getMessage() or 
                "ValidationError" in record.getMessage() or
                "EOF while parsing" in record.getMessage()):
                return False
            return True
    
    # Apply filter to relevant loggers
    for logger_name in ['mcp.client.streamable_http', 'mcp', 'pydantic_core']:
        logger = logging.getLogger(logger_name)
        logger.addFilter(SSEFilter())
    
    console.print(Panel("[bold cyan]🎮 Interactive MCP Client[/bold cyan]", expand=False))
    console.print("[dim]Explore MCP server tools interactively[/dim]\n")
    
    # Check for existing resumption tokens
    token_manager = TokenManager()
    existing_tokens: Dict[str, Any] | None = token_manager.load_tokens()
    
    # Prepare headers for resumption if tokens exist
    headers = {}
    if existing_tokens:
        headers[MCP_SESSION_ID_HEADER] = existing_tokens["session_id"]
        if "protocol_version" in existing_tokens:
            headers[MCP_PROTOCOL_VERSION_HEADER] = existing_tokens["protocol_version"]
        console.print(f"[cyan]🔄 Found existing session, attempting resumption...[/cyan]")
    
    try:
        async with streamablehttp_client(
            server_url,
            headers=headers if headers else None,
            terminate_on_close=False  # Enable resumption
        ) as (read_stream, write_stream, get_session_id):
            
            # Create message handler for real-time notifications
            async def message_handler(message) -> None:
                try:
                    if isinstance(message, types.ServerNotification):
                        if isinstance(message.root, types.LoggingMessageNotification):
                            console.print(f"📡 [dim]{message.root.params.data}[/dim]")
                        elif isinstance(message.root, types.ProgressNotification):
                            progress = message.root.params
                            console.print(f"🔄 [yellow]{progress.message} ({progress.progress}/{progress.total})[/yellow]")
                        elif isinstance(message.root, types.ResourceUpdatedNotification):
                            console.print(f"� [blue]Resource updated: {message.root.params.uri}[/blue]")
                except Exception:
                    # Silently ignore message handler errors
                    pass
            
            # Add sampling callback for research agent
            async def sampling_callback(context, params):
                try:
                    message_text = params.messages[0].content.text if params.messages else 'No message'
                    console.print(f"\n🧠 [bold cyan]Server requested sampling:[/bold cyan]")
                    console.print(f"   [yellow]{message_text}[/yellow]")
                    
                    # Mock response instead of prompting user
                    mock_response = "Based on current research, MCP has evolved significantly with new features like resumable streams, elicitation, and sampling capabilities, enabling sophisticated agent-to-agent communication patterns."
                    
                    console.print(f"[dim]🤖 Auto-responding with mock data:[/dim]")
                    console.print(f"   [green]{mock_response[:80]}...[/green]")
                    
                    return types.CreateMessageResult(
                        role="assistant",
                        content=types.TextContent(
                            type="text",
                            text=mock_response
                        ),
                        model="interactive-client",
                        stopReason="endTurn"
                    )
                except Exception as e:
                    return types.ErrorData(code=-1, message=str(e))
            
            # Add elicitation callback for travel agent  
            async def elicitation_callback(context, params):
                try:
                    console.print(f"\n💬 [bold yellow]Server is asking for confirmation:[/bold yellow]")
                    console.print(f"   [cyan]{params.message}[/cyan]")
                    
                    # Get user's decision
                    while True:
                        response = console.input("\n[bold]Do you accept? (y/n/details): [/bold]").strip().lower()
                        
                        if response in ['y', 'yes', 'accept']:
                            user_notes = console.input("[dim]Any additional notes (optional): [/dim]").strip()
                            console.print(f"[dim]✅ Sending acceptance with notes: '{user_notes or 'Confirmed by user'}'[/dim]")
                            return types.ElicitResult(
                                action="accept",
                                content={
                                    "confirm": True, 
                                    "notes": user_notes if user_notes else "Confirmed by user"
                                }
                            )
                        elif response in ['n', 'no', 'decline']:
                            reason = console.input("[dim]Reason for declining (optional): [/dim]").strip()
                            return types.ElicitResult(
                                action="decline",
                                content={
                                    "confirm": False,
                                    "notes": reason if reason else "Declined by user"
                                }
                            )
                        elif response in ['d', 'details']:
                            console.print(f"[dim]Schema: {params.requestedSchema if hasattr(params, 'requestedSchema') else 'Not specified'}[/dim]")
                        else:
                            console.print("[red]Please enter 'y' (yes), 'n' (no), or 'd' (details)[/red]")
                            
                except Exception as e:
                    console.print(f"[red]Error in elicitation: {e}[/red]")
                    return types.ElicitResult(action="decline", content={"confirm": False, "notes": f"Error: {e}"})
            
            # Add resumption token callback for long-running tools
            async def on_resumption_token_update(session_id: str, resumption_token: str, tool_name: str, tool_args: dict):
                """Callback for when resumption token is updated during long-running operations."""
                # Save the updated token with tool information
                protocol_version = existing_tokens.get("protocol_version") if existing_tokens else None
                token_manager.save_tokens(session_id, resumption_token, protocol_version, tool_name, tool_args)
            
            async with ClientSession(
                read_stream, 
                write_stream, 
                message_handler=message_handler,
                sampling_callback=sampling_callback,
                elicitation_callback=elicitation_callback
            ) as session:
                
                # Handle resumption vs new session based on tokens
                if existing_tokens and existing_tokens.get("resumption_token") and existing_tokens.get("last_tool") and existing_tokens.get("last_args"):
                    # RESUMPTION FLOW: We have everything needed for resumption
                    console.print(f"[cyan]🔄 Resuming existing session...[/cyan]")
                    console.print(f"[cyan]   Session ID: {existing_tokens['session_id']}[/cyan]")
                    console.print(f"[cyan]   Resuming tool: {existing_tokens['last_tool']}[/cyan]")
                    console.print(f"[green]✅ Skipping initialization, directly resuming...[/green]")
                    
                    try:
                        # Directly resume the tool execution with cached data
                        result = await execute_tool_with_resumption(
                            session, 
                            existing_tokens["last_tool"], 
                            existing_tokens["last_args"], 
                            get_session_id, 
                            on_resumption_token_update, 
                            existing_tokens,  # Pass existing tokens for resumption
                            token_manager
                        )
                        console.print(f"[green]✅ Resumed tool completed successfully![/green]")
                        console.print(f"[green]Result:[/green]")
                        console.print(f"   {extract_text_content(result)}")
                        
                        # Task completed successfully, clean up tokens
                        if token_manager.delete_tokens():
                            console.print(f"[dim]🧹 Cleaned up resumption tokens[/dim]")
                        
                        # After successful resumption, continue with normal interactive flow
                        console.print("\n[cyan]📋 Loading available tools for continued interaction...[/cyan]")
                        tools_result = await session.list_tools()
                        tools = tools_result.tools
                        tools_dict = {tool.name: tool for tool in tools}
                        display_tools(tools)
                        
                    except Exception as resume_error:
                        error_msg = str(resume_error)
                        if "ValidationError" in error_msg and "JSON" in error_msg:
                            console.print(f"[yellow]⚠️ Resumed tool completed with connection issues, but likely succeeded[/yellow]")
                            # Even if there was a connection issue, task likely completed
                            if token_manager.delete_tokens():
                                console.print(f"[dim]🧹 Cleaned up resumption tokens[/dim]")
                            
                            # Load tools for continued interaction
                            console.print("\n[cyan]📋 Loading available tools for continued interaction...[/cyan]")
                            tools_result = await session.list_tools()
                            tools = tools_result.tools
                            tools_dict = {tool.name: tool for tool in tools}
                            display_tools(tools)
                        else:
                            console.print(f"[red]❌ Resume failed: {resume_error}[/red]")
                            console.print(f"[yellow]Falling back to normal initialization...[/yellow]")
                            # Fallback to normal initialization
                            result = await session.initialize()
                            console.print(f"[green]✅ Connected to: {result.serverInfo.name}[/green]")
                            tools_result = await session.list_tools()
                            tools = tools_result.tools
                            tools_dict = {tool.name: tool for tool in tools}
                            display_tools(tools)
                else:
                    # NORMAL FLOW: No resumption tokens, do full initialization
                    console.print("[cyan]🔌 Connecting to server...[/cyan]")
                    result = await session.initialize()
                    
                    console.print(f"[green]✅ Connected to: {result.serverInfo.name}[/green]")
                    console.print(f"[green]📋 Protocol: {result.protocolVersion}[/green]")
                    
                    # Save protocol version for future resumption
                    current_session_id = get_session_id()
                    if current_session_id:
                        console.print(f"[green]🆔 Session: {current_session_id}[/green]")
                        
                    
                    # Load and display available tools
                    console.print("\n[cyan]📋 Loading available tools...[/cyan]")
                    tools_result = await session.list_tools()
                    tools = tools_result.tools
                    tools_dict = {tool.name: tool for tool in tools}
                    
                    display_tools(tools)
                
                # Interactive command loop
                console.print("\n[dim]Commands: [tool_name], 'list', 'help', 'clean-tokens', 'quit'[/dim]")
                
                while True:
                    try:
                        command = console.input("\n[bold blue]> [/bold blue]").strip()
                        
                        if command.lower() in ['quit', 'exit', 'q']:
                            console.print("[yellow]👋 Goodbye![/yellow]")
                            break
                            
                        elif command.lower() in ['list', 'l']:
                            display_tools(tools)
                            
                        elif command.lower() in ['help', 'h']:
                            console.print("[bold]Available Commands:[/bold]")
                            console.print("  [cyan]list[/cyan] or [cyan]l[/cyan] - Show available tools")
                            console.print("  [cyan][tool_name][/cyan] - Execute a tool")
                            console.print("  [cyan]help[/cyan] or [cyan]h[/cyan] - Show this help")
                            console.print("  [cyan]clean-tokens[/cyan] - Delete resumption tokens")
                            console.print("  [cyan]quit[/cyan] or [cyan]q[/cyan] - Exit")
                            console.print("\n[bold]Agent tools (try these!):[/bold]")
                            for tool in tools:
                                if "agent" in tool.name.lower():
                                    console.print(f"  🤖 [yellow]{tool.name}[/yellow]")
                        
                        elif command.lower() in ['clean-tokens', 'clean']:
                            if token_manager.delete_tokens():
                                console.print("[green]✅ Resumption tokens cleared[/green]")
                            else:
                                console.print("[yellow]No tokens to clear[/yellow]")
                            
                        elif command in tools_dict:
                            tool = tools_dict[command]
                            
                            # Collect arguments
                            args = {}
                            if tool.inputSchema and tool.inputSchema.get("properties"):
                                console.print(f"[dim]Tool '{command}' parameters:[/dim]")
                                for prop_name, prop_info in tool.inputSchema["properties"].items():
                                    required = prop_name in tool.inputSchema.get("required", [])
                                    default = prop_info.get("default", "")
                                    desc = prop_info.get("description", "")
                                    
                                    prompt = f"  {prop_name}"
                                    if desc:
                                        prompt += f" ({desc})"
                                    if default:
                                        prompt += f" [default: {default}]"
                                    if required:
                                        prompt += " [required]"
                                    prompt += ": "
                                    
                                    value = console.input(prompt).strip()
                                    if value:
                                        # Cast the input value to the correct type
                                        args[prop_name] = cast_input_value(value, prop_info)
                                    elif required and not default:
                                        console.print(f"[red]❌ {prop_name} is required[/red]")
                                        break
                                else:
                                    # All required args collected, execute tool
                                    console.print(f"[cyan]🔧 Executing {command}...[/cyan]")
                                    
                                    try:
                                        result = await execute_tool_with_resumption(
                                            session, command, args, get_session_id, on_resumption_token_update, existing_tokens, token_manager
                                        )
                                        console.print(f"[green]✅ Result:[/green]")
                                        console.print(f"   {extract_text_content(result)}")
                                        
                                        # Task completed successfully, clean up tokens
                                        if token_manager.delete_tokens():
                                            console.print(f"[dim]🧹 Cleaned up resumption tokens[/dim]")
                                        
                                    except Exception as tool_error:
                                        error_msg = str(tool_error)
                                        if "ValidationError" in error_msg and "JSON" in error_msg:
                                            console.print(f"[yellow]⚠️ Tool completed with connection issues, but likely succeeded[/yellow]")
                                            # Even if there was a connection issue, task likely completed
                                            if token_manager.delete_tokens():
                                                console.print(f"[dim]🧹 Cleaned up resumption tokens[/dim]")
                                        else:
                                            console.print(f"[red]❌ Tool failed: {tool_error}[/red]")
                            else:
                                # No parameters needed, execute tool
                                console.print(f"[cyan]🔧 Executing {command}...[/cyan]")
                                
                                try:
                                    result = await execute_tool_with_resumption(
                                        session, command, {}, get_session_id, on_resumption_token_update, existing_tokens, token_manager
                                    )
                                    console.print(f"[green]✅ Result:[/green]")
                                    console.print(f"   {extract_text_content(result)}")
                                    
                                    # Task completed successfully, clean up tokens
                                    if token_manager.delete_tokens():
                                        console.print(f"[dim]🧹 Cleaned up resumption tokens[/dim]")
                                    
                                except Exception as tool_error:
                                    error_msg = str(tool_error)
                                    if "ValidationError" in error_msg and "JSON" in error_msg:
                                        console.print(f"[yellow]⚠️ Tool completed with connection issues, but likely succeeded[/yellow]")
                                        # Even if there was a connection issue, task likely completed
                                        if token_manager.delete_tokens():
                                            console.print(f"[dim]🧹 Cleaned up resumption tokens[/dim]")
                                    else:
                                        console.print(f"[red]❌ Tool failed: {tool_error}[/red]")
                        
                        else:
                            console.print(f"[red]❌ Unknown command: '{command}'[/red]")
                            console.print("[dim]Type 'list' to see available tools or 'help' for commands[/dim]")
                            
                    except KeyboardInterrupt:
                        console.print("\n[yellow]👋 Interrupted![/yellow]")
                        break
    
    except Exception as e:
        console.print(f"[red]❌ Connection error: {e}[/red]")


async def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Interactive MCP Client")
    parser.add_argument("--url", default="http://127.0.0.1:8006/mcp", help="MCP server URL")
    parser.add_argument("--clean-tokens", action="store_true", help="Delete existing resumption tokens and start fresh")
    
    args = parser.parse_args()
    
    # Handle token cleaning
    if args.clean_tokens:
        token_manager = TokenManager()
        if token_manager.delete_tokens():
            console.print("[green]✅ Resumption tokens cleared[/green]")
        else:
            console.print("[yellow]No tokens to clear[/yellow]")
        return
    
    await interactive_mode(args.url)


if __name__ == "__main__":
    # Configure logging to suppress noisy MCP warnings
    logging.basicConfig(level=logging.WARNING)
    
    # Suppress specific noisy loggers
    logging.getLogger('mcp.client.streamable_http').setLevel(logging.ERROR)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Goodbye![/yellow]")
    except Exception as e:
        console.print(f"[red]💥 Fatal error: {e}[/red]")
