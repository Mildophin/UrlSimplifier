from django.db import models


class SimplifiedUrl(models.Model):
    redirection_path = models.CharField(max_length=10)
    url_to_redirect = models.URLField(max_length=200)
