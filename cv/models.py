from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL


class PersonalInfo(models.Model):
    GENDER_CHOICE = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=50,
                               blank=True,
                               null=True,
                               help_text="i.e: Web Developer")

    birth_day = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    nationality = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=200,
                                null=True,
                                blank=True,
                                help_text="Sparate languages by comma"
                                )

    interest = models.CharField(max_length=400,
                                null=True,
                                blank=True,
                                help_text="Sparate interests by comma"
                                )

    skills = models.CharField(max_length=400,
                              null=True,
                              blank=True,
                              help_text="Sparate Skills by comma"
                              )

    bio = models.TextField()
    picture = models.ImageField(null=True, blank=True,
                                height_field="height_field",
                                width_field="width_field"
                                )

    height_field = models.IntegerField(default=600,
                                       null=True,
                                       blank=True,
                                       )

    width_field = models.IntegerField(default=600,
                                      null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user.username)

    def get_update_url(self):
        return reverse("update_personal_info", kwargs={"pk": self.pk})

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class WorkExperience(models.Model):
    user = models.ForeignKey(User, related_name="works")
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    joining_year = models.DateField()
    job_description = models.TextField()

    def get_delete_url(self):
        return reverse("delete_work_experience", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_work_experience", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user.username)


class Education(models.Model):
    user = models.ForeignKey(User, related_name="educations")
    institute_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    year = models.DateField()
    description = models.TextField()

    def get_delete_url(self):
        return reverse("delete_education", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_education", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user.username)
