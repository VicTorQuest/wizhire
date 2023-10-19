from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from localflavor.us.models import USStateField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.utils.text import gettext_lazy as _



User = get_user_model()
# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    

class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100, help_text="Ex: Software Engineer")
    company = models.CharField(max_length=100, help_text="Ex: Microsoft")
    location = models.CharField(max_length=100, help_text="The address of the company")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Can be null for current job
    description = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=100, help_text="Ex: University of Nigeria")
    degree = models.CharField(max_length=100, help_text="Ex: Bachelors")
    field_of_study = models.CharField(max_length=100, help_text="Ex: Computer Science")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  
    description = models.TextField(help_text="Describe your studies, awards, e.t.c")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    country = CountryField(default='NG')  # Default country is set to the United States
    state = USStateField(blank=True, null=True)  # Allow state to be blank
    address = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=6, validators=[RegexValidator('^[0-9]*$', _('Invalid postal code'))],)
    date_of_birth = models.DateField(null=True)
    professional_role = models.CharField(max_length=250, help_text='Add a title to tell the world what you do.')
    work_experiences = models.ManyToManyField(WorkExperience, related_name='work_experiences')
    educations = models.ManyToManyField(Education, related_name='educations', help_text="You don’t have to have a degree. Adding any relevant education helps make your profile more visible.")
    skills = models.ManyToManyField(Skill, help_text="Your skills show clients what you can offer, and help us choose which jobs to recommend to you.")
    languages = models.ManyToManyField(Language, help_text="clients are often interested to know what languages you speak. English is a must, but do you speak any other languages?")
    bio = models.TextField()
    services = models.ManyToManyField(Service, help_text="Choose at least one service that best describes the type of work you do. This helps us match you with clients who need your unique expertise.")



