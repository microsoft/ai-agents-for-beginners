#!/usr/bin/env python3
"""
Resumable MCP Server Implementation

This server provides full session resumption capabilities using an event store.
It supports long-running tasks that can be resumed after client disconnection.
"""

import argparse
import asyncio
import logging
import re
from turtle import st
from typing import Optional

import anyio
import uvicorn
from pydantic import AnyUrl
from starlette.applications import Starlette
from starlette.routing import Mount
from pydantic import BaseModel, Field
from mcp.server import Server
from mcp.server.streamable_http import EventStore
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from mcp.server.transport_security import TransportSecuritySettings
from mcp.types import TextContent, Tool, SamplingMessage

from .event_store import SimpleEventStore

logger = logging.getLogger(__name__)


                            
class PriceConfirmationSchema(BaseModel):
    confirm: bool = Field(description="Confirm the price for this trip")
    notes: str = Field(default="", description="Any additional notes about the price")
                            
class ResumableServer(Server):
    """Server implementation with long-running tools and notifications for resumption testing."""

    def __init__(self, name: str = "resumable_mcp_server"):
        super().__init__(name)
        logger.info(f"ResumableServer '{name}' initialized")

        @self.list_tools()
        async def handle_list_tools() -> list[Tool]:
            """List available tools including resumable ones."""
            return [
                Tool(
                    name="travel_agent",
                    description="Book a travel trip with progress updates and price confirmation",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "destination": {
                                "type": "string",
                                "description": "Travel destination",
                                "default": "Paris"
                            }
                        }
                    },
                ),
                Tool(
                    name="research_agent",
                    description="Research a topic with progress updates and interactive summaries",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "topic": {
                                "type": "string",
                                "description": "Research topic",
                                "default": "AI trends"
                            }
                        }
                    },
                ),
                Tool(
                    name="long_running_agent",
                    description="A long-running task for testing resumption (50 steps, 2 seconds each)",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    },
                ),
            ]

        @self.call_tool()
        async def handle_call_tool(name: str, args: dict) -> list[TextContent]:
            """Handle tool execution with support for long-running tasks."""
            ctx = self.request_context
            logger.info(f"Tool called: {name} with args: {args}")

            if name == "travel_agent":
                destination = args.get("destination", "Paris")
                logger.info(f"Travel agent: destination={destination}")
                
                # Simple travel booking flow with progress updates
                steps = [
                    "Checking flights...",
                    "Finding available dates...", 
                    "Confirming prices...",
                    "Booking flight..."
                ]
                
                elicitation_result = None
                booking_cancelled = False
                
                for i, step in enumerate(steps):
                    await ctx.session.send_progress_notification(
                        progress_token=ctx.request_id,
                        progress=i * 25,
                        total=100,
                        message=step, 
                        related_request_id=str(ctx.request_id)   
                    )
                    
                    # Add elicitation request at step 3 (Confirming prices)
                    if i == 2:  # "Confirming prices..." step
                        try:
                            elicit_result = await ctx.session.elicit(
                                message=f"Please confirm the estimated price of $1200 for your trip to {destination}",
                                requestedSchema=PriceConfirmationSchema.model_json_schema(),
                                related_request_id=ctx.request_id,
                            )
                            
                            elicitation_result = elicit_result
                            
                            if elicit_result and elicit_result.action == "accept":
                                logger.info(f"User confirmed price: {elicit_result.content}")
                                # Continue with booking
                            elif elicit_result and elicit_result.action == "decline":
                                logger.info(f"User declined price confirmation: {elicit_result.content}")
                                booking_cancelled = True
                                # Stop the booking process
                                await ctx.session.send_progress_notification(
                                    progress_token=ctx.request_id,
                                    progress=100,
                                    total=100,
                                    message="Booking cancelled by user",
                                    related_request_id= str(ctx.request_id)
                                )
                                break
                            else:
                                logger.info("User cancelled elicitation")
                                booking_cancelled = True
                                await ctx.session.send_progress_notification(
                                    progress_token=ctx.request_id,
                                    progress=100,
                                    total=100,
                                    message="Booking cancelled"
                                )
                                break
                                
                        except Exception as e:
                            logger.info(f"Elicitation request failed (this is normal in tests): {e}")
                            # Continue with booking anyway for fallback
                    
                    if not booking_cancelled:
                        await anyio.sleep(2)  # Fixed 0.5 second delay between steps
                
                # Generate final result based on elicitation outcome
                if booking_cancelled:
                    if elicitation_result and hasattr(elicitation_result, 'content') and elicitation_result.content:
                        notes = elicitation_result.content.get('notes', 'No reason provided')
                        result_text = f"❌ Booking cancelled for trip to {destination}. Reason: {notes}"
                    else:
                        result_text = f"❌ Booking cancelled for trip to {destination}."
                else:
                    # Final progress update for successful booking
                    await ctx.session.send_progress_notification(
                        progress_token=ctx.request_id,
                        progress=100,
                        total=100,
                        message="Trip booked successfully"
                    )
                    
                    # Include confirmation details in success message
                    if elicitation_result and elicitation_result.action == "accept" and elicitation_result.content:
                        notes = elicitation_result.content.get('notes', 'No additional notes')
                        result_text = f"✅ Trip booked successfully to {destination}! Price confirmed with notes: '{notes}'"
                    else:
                        result_text = f"✅ Trip booked successfully to {destination}!"

                return [TextContent(type="text", text=result_text)]

            elif name == "research_agent":
                topic = args.get("topic", "AI trends")
                logger.info(f"Research agent: topic={topic}")
                
                # Simple research flow with progress updates
                steps = [
                    "Gathering sources...",
                    "Analyzing data...", 
                    "Summarizing findings...",
                    "Finalizing report..."
                ]
                
                sampling_summary = None
                
                for i, step in enumerate(steps):
                    await ctx.session.send_progress_notification(
                        progress_token=ctx.request_id,
                        progress=i * 25,
                        total=100,
                        message=step
                    )
                    
                    # Add sampling request at step 3 (Summarizing findings)
                    if i == 2:  # "Summarizing findings..." step
                        try:
                            sampling_result = await ctx.session.create_message(
                                messages=[
                                    SamplingMessage(
                                        role="user",
                                        content=TextContent(type="text", text=f"Please summarize the key findings for research on: {topic}")
                                    )
                                ],
                                max_tokens=100,
                                related_request_id=ctx.request_id,
                            )
                            
                            if sampling_result and sampling_result.content:
                                if sampling_result.content.type == "text":
                                    sampling_summary = sampling_result.content.text
                                    logger.info(f"Received sampling summary: {sampling_summary}")
                                    
                        except Exception as e:
                            logger.info(f"Sampling request failed (this is normal in tests): {e}")
                    
                    await anyio.sleep(2)  # Fixed 0.5 second delay between steps
                
                # Final progress update
                await ctx.session.send_progress_notification(
                    progress_token=ctx.request_id,
                    progress=100,
                    total=100,
                    message="Research completed successfully"
                )

                # Use sampling summary if available, otherwise default message
                if sampling_summary:
                    result_text = f"🔍 Research on '{topic}' completed successfully!\n\n📊 Key Findings (from user input): {sampling_summary}"
                else:
                    result_text = f"🔍 Research on '{topic}' completed successfully!"
                
                return [TextContent(type="text", text=result_text)]

            elif name == "long_running_agent":
                # Fixed values optimized for resumption testing
                steps = 50
                duration = 2.0
                logger.info(f"Long running agent: {steps} steps, {duration}s each")
                
                # Send initial log message
                await ctx.session.send_log_message(
                    level="info",
                    data="Long-running task started",
                    logger="long_running_agent",
                    related_request_id=ctx.request_id,
                )
                
                # Execute the long-running task
                for i in range(steps):
                    current_step = i + 1
                    # Use integer arithmetic to avoid floating point precision issues
                    progress_percent = (current_step * 100) // steps
                    
                    # Send log message for each step
                    await ctx.session.send_log_message(
                        level="info",
                        data=f"Processing step {current_step}/{steps} ({progress_percent}%)",
                        logger="long_running_agent",
                        related_request_id=ctx.request_id,
                    )
                    
                    # Wait for 2 seconds
                    await anyio.sleep(duration)
                
                # Send completion log message
                await ctx.session.send_log_message(
                    level="info",
                    data=f"Task completed successfully! Processed {steps} steps in {steps * duration:.0f} seconds.",
                    logger="long_running_agent",
                    related_request_id=ctx.request_id,
                )
                
                # Final completion message
                result_text = f"✅ Long-running task completed successfully! Processed {steps} steps in {steps * duration:.0f} seconds."
                return [TextContent(type="text", text=result_text)]

            else:
                raise ValueError(f"Unknown tool: {name}")


def create_server_app(event_store: Optional[EventStore] = None) -> Starlette:
    """Create the Starlette application with resumable MCP server."""
    # Create server instance
    server = ResumableServer()

    # Create security settings
    security_settings = TransportSecuritySettings(
        allowed_hosts=["127.0.0.1:*", "localhost:*"],
        allowed_origins=["http://127.0.0.1:*", "http://localhost:*"]
    )

    # Create session manager with event store
    session_manager = StreamableHTTPSessionManager(
        app=server,
        event_store=event_store,
        json_response=False,  # Use SSE streams
        security_settings=security_settings,
    )

    # Create ASGI application
    app = Starlette(
        debug=True,
        routes=[
            Mount("/mcp", app=session_manager.handle_request),
        ],
        lifespan=lambda app: session_manager.run(),
    )

    return app


async def run_server(port: int = 8006, with_event_store: bool = True) -> None:
    """Run the resumable HTTP server."""
    # Create event store if requested
    event_store = SimpleEventStore() if with_event_store else None
    
    # Create application
    app = create_server_app(event_store)

    # Configure server
    config = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=port,
        log_level="info",
        limit_concurrency=10,
        timeout_keep_alive=30,
        access_log=True,
    )

    logger.info(f"Starting Resumable HTTP MCP Server on http://127.0.0.1:{port}/mcp")
    if event_store:
        logger.info("Event store enabled - resumption supported")
    else:
        logger.info("Event store disabled - no resumption support")

    # Start the server
    server = uvicorn.Server(config=config)
    
    try:
        await server.serve()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Resumable HTTP MCP Server")
    parser.add_argument("--port", type=int, default=8006, help="Port to listen on (default: 8006)")
    parser.add_argument("--no-event-store", action="store_true", help="Disable event store (no resumption)")
    
    args = parser.parse_args()
    
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Run the server
    asyncio.run(run_server(
        port=args.port,
        with_event_store=not args.no_event_store
    ))


if __name__ == "__main__":
    main()
