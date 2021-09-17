from django.db import models


class Event(models.model):
    description = models.TextField(blank=False)
    target_frequency = models.FloatField(blank=False)
    project = models.ForeignKey("app_label.Project", on_delete=models.CASCADE)


class Cause(models.model):
    description = models.TextField(blank=False)
    initial_frequency = models.FloatField(blank=False)
    project = models.ForeignKey("app_label.Project", on_delete=models.CASCADE)


class CauseBarrier(models.model):
    description = models.TextField(blank=False)
    pfd = models.FloatField(blank=False)
    project = models.ForeignKey("app_label.Project", on_delete=models.CASCADE)


class Consequence(models.model):
    description = models.TextField(blank=False)
    target_frequency = models.FloatField(blank=False)
    project = models.ForeignKey("app_label.Project", on_delete=models.CASCADE)


class ConsequenceBarrier(models.model):
    description = models.TextField(blank=False)
    pfd = models.FloatField(blank=False)
    project = models.ForeignKey("app_label.Project", on_delete=models.CASCADE)


class Project(models.model):
    name = models.TextField(blank=False)
    description = models.TextField(blank=False)
