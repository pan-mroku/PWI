from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    uuid=models.CharField(max_length=50)
    user=models.ForeignKey(User)
    message=models.CharField(max_length=200)
    timestamp=models.DateTimeField()
    
    def Message(self):
        self.uuid=uuid4()
        self.timestamp=timezone.now()

    def __unicode__(self):
        return str(self.timestamp)+" "+str(self.user)+": "+self.message

