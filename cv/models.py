from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    GENDER_CHOICE = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_day = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    nationality = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=14, blank=True)
    email = models.EmailField()
    website = models.URLField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    language_skills = models.CharField(max_length=200,
                                       blank=True, 
                                       help_text="Sparate languages by comma"
                                      )

    other_skills = models.CharField(max_length=200,
                                    blank=True, 
                                    help_text="Sparate Skills by comma"
                                   )

    bio = models.TextField()
    picture = models.ImageField(null=True, blank=True,
                                height_field="height_field",
                                width_field="width_field"
                               )

    height_field = models.IntegerField(default=600)
    width_field = models.IntegerField(default=600)

    def __str__(self):
        return self.user.username


class WorkExperience(models.Model):
    user = models.ForeignKey(User)
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=20)
    joining_year = models.DateField()
    job_description = models.TextField()

    def __str__(self):
        return self.user.username
      

class Education(models.Model):
    user = models.ForeignKey(User)
    institute_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=40)
    year = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.user.username
 