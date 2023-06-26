from django.db import models
from django.utils.translation import gettext_lazy as _


class Uniform(models.Model):
    class Meta:
        verbose_name = _('Uniform')
        verbose_name_plural = _('Uniforms')

    name = models.CharField(max_length=50, db_index=True, verbose_name=_('name'))
    description = models.CharField(max_length=100, null=False, blank=False, db_index=True, verbose_name=_('description'))
    size = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('size'))


    def __str__(self):
        return f"{_('Uniform')}(pk={self.pk}, name={self.name!r})"
