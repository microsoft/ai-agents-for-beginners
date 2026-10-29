import unittest
from unittest.mock import AsyncMock

from anyio import ClosedResourceError
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

    async def asyncTearDown(self) -> None:
        self.store.close()

    async def test_returns_stream_when_no_later_events_exist(self) -> None:
        last_event_id = await self.store.store_event(
            "stream-a", message("notifications/first")
        )

        callback = AsyncMock()
        stream_id = await self.store.replay_events_after(last_event_id, callback)

        self.assertEqual(stream_id, "stream-a")
        callback.assert_not_awaited()

    async def test_callback_failure_stops_replay_and_can_be_retried(self) -> None:
        last_event_id = await self.store.store_event(
            "stream-a", message("notifications/first")
        )
        expected_ids = [
            await self.store.store_event("stream-a", message("notifications/second")),
            await self.store.store_event("stream-a", message("notifications/third")),
        ]
        for error in (BrokenPipeError("client disconnected"), ClosedResourceError()):
            with self.subTest(error=type(error).__name__):
                failed_callback = AsyncMock(side_effect=error)

                with self.assertRaises(type(error)) as raised:
                    await self.store.replay_events_after(last_event_id, failed_callback)

                self.assertIs(raised.exception, error)
                failed_callback.assert_awaited_once()
                self.assertEqual(
                    failed_callback.await_args.args[0].event_id, expected_ids[0]
                )

        callback = AsyncMock()
        stream_id = await self.store.replay_events_after(last_event_id, callback)

        self.assertEqual(stream_id, "stream-a")
        self.assertEqual(
            [call.args[0].event_id for call in callback.await_args_list],
            expected_ids,
        )

    async def test_invalid_json_is_skipped_before_replaying_valid_event(self) -> None:
        last_event_id = await self.store.store_event(
            "stream-a", message("notifications/first")
        )
        self.store._store_event_sync("stream-a", "invalid json")
        expected = message("notifications/valid")
        expected_id = await self.store.store_event("stream-a", expected)
        callback = AsyncMock()

        with self.assertLogs("event_store", level="ERROR") as logs:
            stream_id = await self.store.replay_events_after(last_event_id, callback)

        self.assertIn("Failed to deserialize event", logs.output[0])
        self.assertEqual(stream_id, "stream-a")
        callback.assert_awaited_once()
        replayed = callback.await_args.args[0]
        self.assertEqual(replayed.event_id, expected_id)
        self.assertEqual(replayed.message, expected)


if __name__ == "__main__":
    unittest.main()
