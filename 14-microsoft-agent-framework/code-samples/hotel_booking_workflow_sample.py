# Copyright (c) Microsoft. All rights reserved.

"""
Sample: Hotel Booking Conditional Workflow

This sample demonstrates a conditional workflow using the Microsoft Agent Framework
that routes based on hotel availability.

Workflow:
1. User provides a destination city
2. Agent checks hotel availability using a tool
3. Conditional routing:
   - If NO availability → Suggest alternative city
   - If availability → Suggest booking
4. Display result with HTML formatting

Key Concepts:
- WorkflowBuilder with conditional edges
- AgentExecutor wrapping AI agents
- @executor decorator for custom logic
- Pydantic models for structured outputs
- @ai_function decorator for tools
- OpenAIChatClient integration
"""

import asyncio
import json
import os
from typing import Annotated, Any, Never

from agent_framework import (
    AgentExecutor,
    AgentExecutorRequest,
    AgentExecutorResponse,
    ChatMessage,
    Role,
    WorkflowBuilder,
    WorkflowContext,
    ai_function,
    executor,
)
from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv
from pydantic import BaseModel

# ============================================================================
# STEP 1: PYDANTIC MODELS FOR STRUCTURED OUTPUTS
# ============================================================================


class BookingCheckResult(BaseModel):
    """Result from checking hotel availability at a destination."""

    destination: str
    has_availability: bool
    message: str


class AlternativeResult(BaseModel):
    """Suggested alternative destination when no rooms available."""

    alternative_destination: str
    reason: str


class BookingConfirmation(BaseModel):
    """Booking suggestion when rooms are available."""

    destination: str
    action: str
    message: str


# ============================================================================
# STEP 2: HOTEL BOOKING TOOL (AI FUNCTION)
# ============================================================================


@ai_function(description="Check hotel room availability for a destination city")
def hotel_booking(destination: Annotated[str, "The destination city to check for hotel rooms"]) -> str:
    """
    Simulates checking hotel room availability.

    For demo purposes:
    - Stockholm, Seattle, Tokyo have rooms
    - All other cities don't have rooms

    Returns:
        JSON string with availability status
    """
    print(f"🔍 Checking hotel availability in {destination}...")

    # Simulate availability check
    cities_with_rooms = ["stockholm", "seattle", "tokyo", "london", "amsterdam"]
    has_rooms = destination.lower() in cities_with_rooms

    result = {"has_availability": has_rooms, "destination": destination}

    return json.dumps(result)


# ============================================================================
# STEP 3: CONDITION FUNCTIONS FOR ROUTING
# ============================================================================


def has_availability_condition(message: Any) -> bool:
    """
    Condition for routing when hotels ARE available.

    Args:
        message: Message from upstream executor (should be AgentExecutorResponse)

    Returns:
        True if availability exists, False otherwise
    """
    if not isinstance(message, AgentExecutorResponse):
        return True  # Default to True if not the expected type

    try:
        result = BookingCheckResult.model_validate_json(message.agent_run_response.text)
        print(f"✅ Availability check: {result.has_availability} for {result.destination}")
        return result.has_availability
    except Exception as e:
        print(f"⚠️  Error parsing availability result: {e}")
        return False


def no_availability_condition(message: Any) -> bool:
    """
    Condition for routing when hotels are NOT available.

    Args:
        message: Message from upstream executor

    Returns:
        True if no availability, False otherwise
    """
    if not isinstance(message, AgentExecutorResponse):
        return False

    try:
        result = BookingCheckResult.model_validate_json(message.agent_run_response.text)
        print(f"❌ No availability for {result.destination}")
        return not result.has_availability
    except Exception as e:
        print(f"⚠️  Error parsing availability result: {e}")
        return False


# ============================================================================
# STEP 4: DISPLAY EXECUTOR (Custom transformation)
# ============================================================================


@executor(id="display_result")
async def display_result(response: AgentExecutorResponse, ctx: WorkflowContext[Never, str]) -> None:
    """
    Display the final result as workflow output.

    This executor receives the final agent response and yields it as output.
    """
    print(f"📤 Yielding workflow output...")
    await ctx.yield_output(response.agent_run_response.text)


# ============================================================================
# STEP 5: MAIN WORKFLOW FUNCTION
# ============================================================================


async def main() -> None:
    """
    Main function to build and execute the hotel booking workflow.
    """
    # Load environment variables
    load_dotenv()

    # Verify configuration
    print("=" * 80)
    print("🏨 HOTEL BOOKING CONDITIONAL WORKFLOW")
    print("=" * 80)

    # GitHub Models or Azure OpenAI
    openai_api_key = os.getenv("OPENAI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")
    chat_client = OpenAIChatClient(base_url=os.environ.get(
        "GITHUB_ENDPOINT"), api_key=os.environ.get("GITHUB_TOKEN"), model_id="gpt-4o")



    print("\n" + "=" * 80)
    print("STEP 1: Creating AI Agents with Structured Outputs")
    print("=" * 80)

    # Agent 1: Check availability
    availability_agent = AgentExecutor(
        chat_client.create_agent(
            instructions=(
                "You are a hotel booking assistant that checks room availability. "
                "Use the hotel_booking tool to check if rooms are available at the destination. "
                "Return JSON with fields: destination (string), has_availability (bool), and message (string). "
                "The message should summarize the availability status."
            ),
            tools=[hotel_booking],
            response_format=BookingCheckResult,
        ),
        id="availability_agent",
    )
    print("✅ Created availability_agent with hotel_booking tool")

    # Agent 2: Suggest alternative (when no rooms)
    alternative_agent = AgentExecutor(
        chat_client.create_agent(
            instructions=(
                "You are a helpful travel assistant. When a user cannot find hotels in their requested city, "
                "suggest an alternative nearby city that has availability. "
                "Return JSON with fields: alternative_destination (string) and reason (string). "
                "Choose from: Stockholm, Seattle, Tokyo, London, or Amsterdam (these have rooms). "
                "Make your suggestion sound appealing and helpful."
            ),
            response_format=AlternativeResult,
        ),
        id="alternative_agent",
    )
    print("✅ Created alternative_agent for suggesting other cities")

    # Agent 3: Suggest booking (when rooms available)
    booking_agent = AgentExecutor(
        chat_client.create_agent(
            instructions=(
                "You are a booking assistant. The user has found available hotel rooms. "
                "Encourage them to book by highlighting the destination's appeal. "
                "Return JSON with fields: destination (string), action (string), and message (string). "
                "The action should be 'book_now' and message should be encouraging."
            ),
            response_format=BookingConfirmation,
        ),
        id="booking_agent",
    )
    print("✅ Created booking_agent for confirming bookings")

    print("\n" + "=" * 80)
    print("STEP 2: Building Workflow with Conditional Edges")
    print("=" * 80)

    # Build the workflow
    workflow = (
        WorkflowBuilder()
        .set_start_executor(availability_agent)
        # NO AVAILABILITY PATH: availability_agent → alternative_agent → display_result
        .add_edge(availability_agent, alternative_agent, condition=no_availability_condition)
        .add_edge(alternative_agent, display_result)
        # HAS AVAILABILITY PATH: availability_agent → booking_agent → display_result
        .add_edge(availability_agent, booking_agent, condition=has_availability_condition)
        .add_edge(booking_agent, display_result)
        .build()
    )

    print("✅ Workflow built with conditional routing:")
    print("   - If NO availability → suggest alternative")
    print("   - If availability → suggest booking")

    # ============================================================================
    # TEST CASE 1: City WITHOUT availability (Paris)
    # ============================================================================
    print("\n" + "=" * 80)
    print("TEST CASE 1: Checking Paris (NO AVAILABILITY)")
    print("=" * 80)

    request1 = AgentExecutorRequest(
        messages=[ChatMessage(Role.USER, text="I want to book a hotel in Paris")], should_respond=True
    )

    events1 = await workflow.run(request1)
    outputs1 = events1.get_outputs()

    if outputs1:
        print("\n📊 WORKFLOW OUTPUT (Paris):")
        print("-" * 80)
        result1 = AlternativeResult.model_validate_json(outputs1[0])
        print(f"🏨 Alternative Destination: {result1.alternative_destination}")
        print(f"💡 Reason: {result1.reason}")
        print("-" * 80)

    # ============================================================================
    # TEST CASE 2: City WITH availability (Stockholm)
    # ============================================================================
    print("\n" + "=" * 80)
    print("TEST CASE 2: Checking Stockholm (HAS AVAILABILITY)")
    print("=" * 80)

    request2 = AgentExecutorRequest(
        messages=[ChatMessage(Role.USER, text="I want to book a hotel in Stockholm")], should_respond=True
    )

    events2 = await workflow.run(request2)
    outputs2 = events2.get_outputs()

    if outputs2:
        print("\n📊 WORKFLOW OUTPUT (Stockholm):")
        print("-" * 80)
        result2 = BookingConfirmation.model_validate_json(outputs2[0])
        print(f"🏨 Destination: {result2.destination}")
        print(f"✅ Action: {result2.action}")
        print(f"💬 Message: {result2.message}")
        print("-" * 80)

    print("\n" + "=" * 80)
    print("✅ WORKFLOW DEMO COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
