from django.db import models


class FullName(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=256)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'ФИО'
        verbose_name_plural = 'ФИО'
