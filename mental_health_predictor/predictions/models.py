from django.db import models

class UsageData(models.Model):
    user_id = models.CharField(max_length=100)
    screen_time = models.FloatField()
    call_logs = models.IntegerField()
    message_frequency = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
