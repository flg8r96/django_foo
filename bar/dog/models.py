from django.db import models

eventTypeMaxLength = 10
macAddressMaxLength = 48
maxTemperature = 200
# buckleData = 1 represents buckled, 0 represents not buckled


class datasink(models.Model):
    eventDate = models.DateTimeField('event date')
    eventType = models.CharField(max_length = eventTypeMaxLength)
    macAddress = models.CharField(max_length = macAddressMaxLength)
    temperatureData = models.DecimalField(max_digits=maxTemperature, decimal_places=1)
    buckleData = models.BooleanField()

    #def __str__(self):
    #    return self.macAddress

    def __unicode__(self):
        return u'MAC:%s, Event: %s, Temp: %d, ' % (self.macAddress, self.eventType, self.temperatureData)
