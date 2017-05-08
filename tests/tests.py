from django.test import TestCase

from amqp_2phase import events, models


class TestEventCreate(TestCase):
    def test_create_ok(self):
        ev = events.create_event('exchange', 'type', {})
        db_ev = models.AMQPEvent.objects.last()

        self.assertEqual(db_ev.id, ev.id)
        self.assertEqual(db_ev.exchange, 'exchange')
        self.assertEqual(db_ev.event_type, 'type')
        self.assertEqual(db_ev.data, '{}')
        self.assertEqual(db_ev.status, models.EVENT_STATUS_PENDING)
        self.assertIsNotNone(db_ev.create_date)
        self.assertIsNone(db_ev.send_date)

    def test_empty_data(self):
        ev = events.create_event('exchange', 'type', None)
        self.assertEqual(ev.data, '{}')

    def test_empty_type(self):
        with self.assertRaises(ValueError):
            events.create_event('exchange', '', dict())

        with self.assertRaises(ValueError):
            events.create_event('exchange', None, dict())

    def test_empty_exchange(self):
        with self.assertRaises(ValueError):
            events.create_event('', 'type', dict())

        with self.assertRaises(ValueError):
            events.create_event(None, 'type', dict())
