from django.db import models


class AMQPEvent(models.Model):
    exchange = models.CharField(max_length=32, null=False, blank=False)
    data = models.TextField(null=False, blank=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.exchange:
            raise ValueError('{}.exchange cannot be blank.'.format(self.__class__.__name__))

        return super(AMQPEvent, self).save(*args, **kwargs)

    class Meta:
        db_table = 'amqp_events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
