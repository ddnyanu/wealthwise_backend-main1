from django.utils.translation import gettext_lazy as _
from django.db import models

class Role(models.TextChoices):
    FUND_MANAGER = 'Fund Manager', _('Fund Manager')
    ONBOARD_MANAGER = 'Onboard Manager', _('Onboard Manager')
    CLIENT = 'Client', _('Client')

class Gender(models.TextChoices):
    MALE = 'Male', _('Male')
    FEMALE = 'Female', _('Female')
    OTHER = 'Other', _('Other')

class RiskTolerance(models.TextChoices):
    LOW = 'low', _('Low')
    MODERATE = 'moderate', _('Moderate')
    HIGH = 'high', _('High')

class Status(models.IntegerChoices):
    ACTIVE = 1, _('Active')
    INACTIVE = 0, _('Inactive')

class VerificationStatus(models.TextChoices):
    IN_PROGRESS = 'IP', _('In-Progress')
    APPROVED = 'AP', _('Approved')
    REJECTED = 'RJ', _('Rejected')
