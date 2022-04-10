from django.db import models


class Project(models.Model):
    name = models.TextField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True, upload_to="media")
    link = models.URLField(null = True, blank = True)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.TextField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True, upload_to="media")
    link = models.URLField(null = True, blank = True)

    def __str__(self):
        return self.name