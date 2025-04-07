from django.db import models
from authentication.models import CustomUser
from utils.choices import RiskTolerance


class Client(models.Model):
    on_boarding_manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='clients')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    inv_amt = models.PositiveIntegerField()
    exp_returns = models.FloatField()
    risk_tolerance = models.CharField(max_length=10, choices=RiskTolerance.choices)
    inv_duration = models.CharField(max_length=32)
    pref_invest_type = models.CharField(max_length=32)
    emp_status = models.CharField(max_length=32)
    source = models.CharField(max_length=32)
    pan_num = models.CharField(max_length=10)
    aadhar_num = models.CharField(max_length=12)
    gov_id = models.ImageField(upload_to='gov_ids/')

    def __str__(self):
        return self.name