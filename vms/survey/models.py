from django.db import models
from datetime import datetime
import uuid
from django.core.exceptions import ValidationError

'''Site model to store details of each site monitored by DCVMS'''
class Site(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    accomodation = models.BooleanField(default=False)

    def __str__(self):
        return self.name
'''Trusted role'''
class Trusted_role(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

'''Visitors are first stored when they check in for the first time. Subsequent
   checkin updates these fields.'''
class Visitor(models.Model):
    def validate_phone(value):
        allowed = '0123456789(+) -'
        for character in value:
            if str(character) not in allowed:
                raise ValidationError('Invalid phone number provided.')
            elif len(value) < 8 or len(value) > 20:
                raise ValidationError('Phone number must be 8-20 characters long.')

    def validate_name(value):
        for character in value:
            if (str(character).isalpha() is False) and (str(character) != '.' and str(character) != ' '): 
                raise ValidationError('Name must only contain alphabets.')

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False, validators=[validate_name])
    last_name = models.CharField(max_length=50, null=False, blank=False, validators=[validate_name])
    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False, validators=[validate_phone])
    role = models.CharField(max_length=50, null=False, blank=False)
    institution = models.CharField(max_length=50, null=False, blank=False)
    reason = models.CharField(max_length=50, null=True, blank=True)
    checkin = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), editable=False)
    # Stores which site visitor is currently checked in. If visitor is checked out,
    # it stores their last visited site.
    site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)
    trusted_role = models.ForeignKey(Trusted_role, blank=True, null=True, on_delete=models.CASCADE)
    # If visitor is currently in the building, checkout is false. If they sign out,
    # checkout is true.
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


'''Visitors stay details for each visit is logged into this model'''
class History(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    checkin = models.DateTimeField(null=False, blank=False, editable=False)
    checkout = models.DateTimeField(null=False, blank=False, editable=False)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50, null=True, blank=True, editable=False)
    role = models.CharField(max_length=50, null=True, blank=True, editable=False)
    institution = models.CharField(max_length=50, null=True, blank=True, editable=False)
    #trusted_role = models.ForeignKey(Trusted_role, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ("Histories")

    def __str__(self):
        duration = str(self.checkout - self.checkin)
        duration = duration.split(':')
        return "Visit Duration: " + duration[0] + " hours and " + duration[1] + " Minutes"
