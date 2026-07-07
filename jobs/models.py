from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=50)

class Tasks(models.Model):
    task = models.CharField(max_length=50)

class Requirements(models.Model):
    requirement = models.CharField(max_length=50)

class Qualifications(models.Model):
    qualification = models.CharField(max_length=100)

class Job(models.Model):
    job_description = models.TextField()
    url = models.URLField(unique=True)
    company = models.CharField(max_length=50)
    salary = models.IntegerField(default=-1)
    scraped_at = models.DateField(auto_now_add=True)

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Tasks)
    qualifications = models.ManyToManyField(Qualifications)
    requirements = models.ManyToManyField(Requirements)
