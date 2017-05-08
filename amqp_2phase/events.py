import json

from amqp_2phase import models


def create_event(exchange, typ, data):
    if not data:
        data = dict()

    json_data = json.dumps(data)
    ev = models.AMQPEvent(
        exchange=exchange,
        event_type=typ,
        data=json_data
    )
    ev.save()
    return ev
