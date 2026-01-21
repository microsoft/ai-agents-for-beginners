#!/usr/bin/env python3
import asyncio
import os
import sys
from datetime import datetime
from typing import Annotated

# Check for dependencies
try:
    from dotenv import load_dotenv, find_dotenv
    from openai import AsyncOpenAI
    from semantic_kernel import Kernel
    from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
    from semantic_kernel.functions import kernel_function
    from semantic_kernel.contents import ChatHistory
    from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
    from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.open_ai_prompt_execution_settings import OpenAIChatPromptExecutionSettings
except ImportError as e:
    error_message = (
        f"Error importing dependencies: {e}\n"
        "Please install requirements using: pip install -r requirements.txt"
    )
    raise ImportError(error_message) from e

# Load environment variables
load_dotenv(find_dotenv())

# --- Plugins ---

class TimePlugin:
    """A plugin that provides time information."""

    @kernel_function(description="Get the current time and date.")
    def get_current_time(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class CalculatorPlugin:
    """A simple calculator plugin."""

    @kernel_function(description="Add two numbers.")
    def add(self,
            number1: Annotated[float, "The first number"],
            number2: Annotated[float, "The second number"]) -> float:
        return number1 + number2

    @kernel_function(description="Subtract two numbers.")
    def subtract(self,
                 number1: Annotated[float, "The first number"],
                 number2: Annotated[float, "The second number"]) -> float:
        return number1 - number2

# --- Main Agent Logic ---

async def main():
    print("--- Demo AI Agent (Tool Use Pattern) ---")

    # 1. Initialize Kernel
    kernel = Kernel()

    # 2. Add Plugins
    kernel.add_plugin(TimePlugin(), plugin_name="Time")
    kernel.add_plugin(CalculatorPlugin(), plugin_name="Calculator")

    # 3. Configure AI Service
    api_key = os.getenv("GITHUB_TOKEN") or os.getenv("OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "https://models.inference.ai.azure.com/")
    model_id = "gpt-4o-mini" # Common model on GitHub Models

    if not api_key:
        print("\n[WARNING] No API Key found (GITHUB_TOKEN or OPENAI_API_KEY).")
        print("This agent requires an LLM to function.")
        print("You can get a free token from https://github.com/marketplace/models")
        print("\nExiting demonstration setup...")
        return

    print(f"Initializing Service with model: {model_id}")

    # Initialize the Azure OpenAI client (compatible with GitHub Models)
    client = AsyncOpenAI(
        api_key=api_key,
        base_url=endpoint,
    )

    service = OpenAIChatCompletion(
        ai_model_id=model_id,
        async_client=client,
    )
    kernel.add_service(service)

    # 4. Create Chat History and Settings
    chat_history = ChatHistory()
    chat_history.add_system_message(
        "You are a helpful assistant. You have access to a clock and a calculator. "
        "Use them when necessary."
    )

    # Enable auto function calling
    execution_settings = OpenAIChatPromptExecutionSettings(
        function_choice_behavior=FunctionChoiceBehavior.Auto()
    )

    print("\nAgent ready! (Type 'exit' to quit)")
    print("Try asking: 'What time is it?' or 'What is 55 plus 12?'")

    # 5. Chat Loop
    while True:
        try:
            user_input = input("\nUser: ")
        except EOFError:
            break

        if not user_input or user_input.lower() in ["exit", "quit"]:
            break

        chat_history.add_user_message(user_input)

        try:
            # Get response from the agent
            response = await service.get_chat_message_content(
                chat_history=chat_history,
                settings=execution_settings,
                kernel=kernel
            )

            print(f"Agent: {response.content}")
            chat_history.add_message(response)

        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
