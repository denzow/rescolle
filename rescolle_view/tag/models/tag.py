from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return 'Tag({})'.format(self.name)
