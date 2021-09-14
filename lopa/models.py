from django.db import models


class Event(models.Model):
    description = models.TextField(blank=True, null=True)
    target_frequency = models.FloatField(blank=True, null=True)


class Cause(models.Model):
    description = models.TextField(blank=True, null=True)
    initial_frequency = models.FloatField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)


class CauseBarrier(models.Model):
    description = models.TextField(blank=True, null=True)
    pfd = models.FloatField(blank=True, null=True)
    cause_id = models.IntegerField(blank=True, null=True)


class Consequence(models.Model):
    description = models.TextField(blank=True, null=True)
    target_frequency = models.FloatField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)


class ConsequenceBarrier(models.Model):
    description = models.TextField(blank=True, null=True)
    pfd = models.FloatField(blank=True, null=True)
    consequence_id = models.IntegerField(blank=True, null=True)
