from django.db import models


app_label = "lopa"


class BaseModel(models.Model):
    description = models.TextField(blank=False)

    class Meta:
        abstract = True


class Event(BaseModel):
    target_frequency = models.FloatField(blank=False)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)


class Cause(BaseModel):
    initial_frequency = models.FloatField(blank=False)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)


class CauseBarrier(BaseModel):
    pfd = models.FloatField(blank=False)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)


class Consequence(BaseModel):
    target_frequency = models.FloatField(blank=False)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)


class ConsequenceBarrier(BaseModel):
    pfd = models.FloatField(blank=False)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)


class Project(BaseModel):
    title = models.TextField(blank=False)
