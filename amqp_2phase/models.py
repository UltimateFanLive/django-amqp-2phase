from django.db import models


class AMQPEvent(models.Model):
    exchange = models.CharField(max_length=32, null=False, blank=False)
    event_type = models.CharField(max_length=32, null=False, blank=False, db_column='type')
    data = models.TextField(null=False, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'amqp_events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
