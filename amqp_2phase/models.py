from django.db import models

EVENT_STATUS_PENDING = 1
EVENT_STATUS_COMPLETE = 2

EVENT_STATUS_CHOICES = (
    (EVENT_STATUS_PENDING, 'Pending'),
    (EVENT_STATUS_COMPLETE, 'Complete'),
)


class AMQPEvent(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    send_date = models.DateTimeField(null=True, blank=True)
    status = models.SmallIntegerField(choices=EVENT_STATUS_CHOICES, null=False, blank=False,
                                      default=EVENT_STATUS_PENDING)
    exchange = models.CharField(max_length=32, null=False, blank=False)
    event_type = models.CharField(max_length=32, null=False, blank=False, db_column='type')
    data = models.TextField(null=False, blank=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.event_type:
            raise ValueError('{}.event_type cannot be blank.'.format(self.__class__.__name__))

        if not self.exchange:
            raise ValueError('{}.exchange cannot be blank.'.format(self.__class__.__name__))

        return super(AMQPEvent, self).save(*args, **kwargs)

    class Meta:
        db_table = 'amqp_events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
