import uuid

from django.db import models


class Year(models.Model):
    year = models.IntegerField(blank=False, null=False, unique=True, primary_key=True)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Challenge(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField(default=False, null=False)


class Attempt(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    grade = models.IntegerField(null=True, default=None)
    started = models.DateTimeField()
    ended = models.DateTimeField(null=True, default=None, db_index=True)
