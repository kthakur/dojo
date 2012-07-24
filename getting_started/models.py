from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
        user = models.ForeignKey(User)
        weight_int = models.CharField(blank=True, max_length=200)
        weight_dec = models.CharField(blank=True, max_length=200)
        morning_drug_size = models.CharField(blank=True, max_length=200)
        morning_drug_amount_int = models.CharField(blank=True, max_length=200)
        morning_drug_amount_dec = models.CharField(blank=True, max_length=200)
        afternoon_drug_size = models.CharField(blank=True, max_length=200)
        afternoon_drug_amount_int = models.CharField(blank=True, max_length=200)
        afternoon_drug_amount_dec = models.CharField(blank=True, max_length=200)
        evening_drug_size = models.CharField(blank=True, max_length=200)
        evening_drug_amount_int = models.CharField(blank=True, max_length=200)
        evening_drug_amount_dec = models.CharField(blank=True, max_length=200)
        pressure_up_first =     models.CharField(blank=True, max_length=200)
        pressure_down_first = models.CharField(blank=True, max_length=200)
        pressure_up_second = models.CharField(blank=True, max_length=200)
        pressure_down_second = models.CharField(blank=True, max_length=200)
        pressure_up_third = models.CharField(blank=True, max_length=200)
        pressure_down_third = models.CharField(blank=True, max_length=200)
        heartrate_first = models.CharField(blank=True, max_length=200)
        heartrate_second = models.CharField(blank=True, max_length=200)
        heartrate_third = models.CharField(blank=True, max_length=200)
        optional_first = models.CharField(blank=True, max_length=200)
        optional_second = models.CharField(blank=True, max_length=200)
        optional_third = models.CharField(blank=True, max_length=200)
        voicemail = models.CharField(blank=True, max_length=200)
        reply_message = models.CharField(blank=True, max_length=200)
        reply_nurse = models.CharField(blank=True, max_length=200)
        reply_needed = models.BooleanField(default=True)
        def __unicode__(self):
                return str(self.id)+" "+self.user.username
