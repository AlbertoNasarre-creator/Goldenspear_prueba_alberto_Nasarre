from django.db import models

# Create your models here.


class messages(models.Model):

    original = models.CharField(max_length=100,blank=True)
    encripted = models.CharField(max_length=100,blank=True)
    original_crc = models.IntegerField(default=0)
    def __str__(self):
        return self.name


    @classmethod
    def create(cls, original,encripted,original_crc):
        message = cls(original=original,encripted=encripted,original_crc=original_crc)
        message.save()
        return message