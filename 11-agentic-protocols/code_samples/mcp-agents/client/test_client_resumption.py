import json
import os
import unittest
from unittest.mock import AsyncMock

from client.client import execute_tool_with_resumption
from client.utils import TokenManager


class _FakeSession:
    """Minimal stand-in for ClientSession that records the request metadata."""

    def __init__(self) -> None:
        self.protocol_version = "2025-03-26"
        self.metadata = None

    async def send_request(self, request, result_type, metadata=None):
        self.metadata = metadata
        return object()


class ResumptionTokenUpdateTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.token_file = f"test_resumption_tokens_{os.getpid()}.json"
        self.token_manager = TokenManager(token_file=self.token_file)

    def tearDown(self) -> None:
        if os.path.exists(self.token_file):
            os.remove(self.token_file)

    def _saved_tokens(self) -> dict:
        with open(self.token_file) as handle:
            return json.load(handle)

    async def test_fresh_request_registers_token_update_callback(self) -> None:
        session = _FakeSession()
        original_callback = AsyncMock()

        await execute_tool_with_resumption(
            session,
            "long_running_agent",
            {},
            lambda: "session-fresh",
            original_callback,
            None,
            self.token_manager,
        )

        self.assertIsNotNone(session.metadata.on_resumption_token_update)
        self.assertIsNone(session.metadata.resumption_token)

    async def test_resume_request_registers_token_update_callback(self) -> None:
        """Resuming must keep listening for newer tokens, not only replay them."""
        session = _FakeSession()
        original_callback = AsyncMock()

        await execute_tool_with_resumption(
            session,
            "long_running_agent",
            {},
            lambda: "session-resume",
            original_callback,
            {"session_id": "session-resume", "resumption_token": "event-42"},
            self.token_manager,
        )

        self.assertEqual(session.metadata.resumption_token, "event-42")
        self.assertIsNotNone(session.metadata.on_resumption_token_update)

    async def test_newer_token_received_while_resuming_is_persisted(self) -> None:
        session = _FakeSession()
        original_callback = AsyncMock()

        await execute_tool_with_resumption(
            session,
            "long_running_agent",
            {"destination": "Paris"},
            lambda: "session-resume",
            original_callback,
            {"session_id": "session-resume", "resumption_token": "event-42"},
            self.token_manager,
        )

        # The transport hands each new SSE event id to the registered callback.
        await session.metadata.on_resumption_token_update("event-99")

        self.assertEqual(self._saved_tokens()["resumption_token"], "event-99")
        original_callback.assert_awaited_once_with(
            "session-resume", "event-99", "long_running_agent", {"destination": "Paris"}
        )


if __name__ == "__main__":
    unittest.main()
