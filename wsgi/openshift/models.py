from django.db import models
from uuid import uuid4
from django.utils import timezone

class Message(models.Model):
    uuid=models.CharField(max_length=50)
    user=models.CharField(max_length=10)
    message=models.CharField(max_length=200)
    timestamp=models.DateTimeField()
    
    def Message(self):
        self.uuid=uuid4()
        self.timestamp=timezone.now()

    def __unicode__(self):
        return str(self.timestamp)+" "+self.user+": "+self.message
