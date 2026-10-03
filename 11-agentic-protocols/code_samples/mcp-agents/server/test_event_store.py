import unittest
from unittest.mock import AsyncMock

from event_store import PersistentEventStore, SimpleEventStore
from mcp.server.streamable_http import EventMessage
from mcp.types import JSONRPCMessage, JSONRPCNotification


def message(method: str) -> JSONRPCMessage:
    return JSONRPCMessage(root=JSONRPCNotification(jsonrpc="2.0", method=method))


class SimpleEventStoreTests(unittest.IsolatedAsyncioTestCase):
    async def test_replay_is_limited_to_original_stream(self) -> None:
        store = SimpleEventStore()
        first = message("notifications/first")
        other_stream = message("notifications/other")
        expected = message("notifications/expected")

        last_event_id = await store.store_event("stream-a", first)
        await store.store_event("stream-b", other_stream)
        expected_event_id = await store.store_event("stream-a", expected)

        callback = AsyncMock()
        stream_id = await store.replay_events_after(last_event_id, callback)

        self.assertEqual(stream_id, "stream-a")
        callback.assert_awaited_once()
        replayed = callback.await_args.args[0]
        self.assertIsInstance(replayed, EventMessage)
        self.assertEqual(replayed.event_id, expected_event_id)
        self.assertIs(replayed.message, expected)

    async def test_unknown_event_id_does_not_replay(self) -> None:
        store = SimpleEventStore()
        await store.store_event("stream-a", message("notifications/first"))
        callback = AsyncMock()

        stream_id = await store.replay_events_after("missing", callback)

        self.assertIsNone(stream_id)
        callback.assert_not_awaited()

    async def test_returns_stream_when_no_later_events_exist(self) -> None:
        store = SimpleEventStore()
        last_event_id = await store.store_event(
            "stream-a", message("notifications/first")
        )

        callback = AsyncMock()
        stream_id = await store.replay_events_after(last_event_id, callback)

        self.assertEqual(stream_id, "stream-a")
        callback.assert_not_awaited()


class PersistentEventStoreTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.store = PersistentEventStore(":memory:")
        self.addCleanup(self.store.close)

    async def test_replay_is_limited_to_original_stream(self) -> None:
        last_event_id = await self.store.store_event(
            "stream-a", message("notifications/first")
        )
        await self.store.store_event("stream-b", message("notifications/other"))
        expected = message("notifications/expected")
        expected_event_id = await self.store.store_event("stream-a", expected)

        callback = AsyncMock()
        stream_id = await self.store.replay_events_after(last_event_id, callback)

        self.assertEqual(stream_id, "stream-a")
        callback.assert_awaited_once()
        replayed = callback.await_args.args[0]
        self.assertIsInstance(replayed, EventMessage)
        self.assertEqual(replayed.event_id, expected_event_id)
        self.assertEqual(replayed.message, expected)

    async def test_unknown_or_invalid_event_id_does_not_replay(self) -> None:
        await self.store.store_event("stream-a", message("notifications/first"))
        for last_event_id in ("999", "missing"):
            with self.subTest(last_event_id=last_event_id):
                callback = AsyncMock()

                stream_id = await self.store.replay_events_after(
                    last_event_id, callback
                )

                self.assertIsNone(stream_id)
                callback.assert_not_awaited()

    async def test_returns_stream_when_no_later_events_exist(self) -> None:
        last_event_id = await self.store.store_event(
            "stream-a", message("notifications/first")
        )
        callback = AsyncMock()

        stream_id = await self.store.replay_events_after(last_event_id, callback)

        self.assertEqual(stream_id, "stream-a")
        callback.assert_not_awaited()

    async def test_returns_stream_when_only_other_stream_has_later_events(self) -> None:
        last_event_id = await self.store.store_event(
            "stream-a", message("notifications/first")
        )
        await self.store.store_event("stream-b", message("notifications/other"))
        callback = AsyncMock()

        stream_id = await self.store.replay_events_after(last_event_id, callback)

        self.assertEqual(stream_id, "stream-a")
        callback.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
