from django.db import models


class Photo(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64, blank=True)
    images = models.ImageField(verbose_name='Фотография', upload_to='img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
