from django.db import models

from djangocms_filer_video.fields.video import FilerVideoFileField


class ExampleModel(models.Model):
    main_video = FilerVideoFileField(verbose_name='Main video', blank=True, null=True,
                                     on_delete=models.SET_NULL,
                                     related_name='example_model_video')


