from django.db import models
from django.utils.translation import gettext_lazy as _

from briefing.models import Briefing
from document.models import Document
from uniform.models import Uniform


def foto_directory_path(instance: "Worker", filename: str) -> str:
    return "foto/foto_{pk}/copy/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Worker(models.Model):
    class Meta:
        verbose_name = _('Worker')
        verbose_name_plural = _('Workers')

    first_name = models.CharField(max_length=30, db_index=True, verbose_name=_('first_name'))
    second_name = models.CharField(max_length=50, db_index=True, verbose_name=_('second_name'))
    middle_name = models.CharField(max_length=30, db_index=True, verbose_name=_('middle_name'))
    foto = models.ImageField(null=True, blank=True, upload_to=foto_directory_path, verbose_name=_('foto'))
    phone = models.CharField(max_length=12, db_index=True, help_text=_("format data: +70001112233"),
                             verbose_name=_('phone'))
    address = models.CharField(max_length=150, null=False, blank=False, db_index=True, verbose_name=_('address'))
    date_birth = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                  help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_birth'))
    data_employment = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data_employment'))
    department = models.CharField(max_length=25, null=False, blank=False, db_index=True, verbose_name=_(
        'department'))  # тут сделать выбор из предустановленных наименований отделов и служб
    position = models.CharField(max_length=30, null=False, blank=False, db_index=True, verbose_name=_('position'))
    category = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('category'))
    electrical_safety_qualification = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True,
                                                               verbose_name=_('electrical_safety_qualification'))
    size_shoe = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('size_shoe'))
    size_clothing = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True,
                                             verbose_name=_('size_clothing'))
    size_hat = models.SmallIntegerField(default=0, null=True, blank=True, db_index=True, verbose_name=_('size_hat'))
    briefings = models.ManyToManyField(Briefing, related_name="briefings", verbose_name=_('briefings'))
    documents = models.ManyToManyField(Document, related_name="documents", verbose_name=_('documents'))
    uniforms = models.ManyToManyField(Uniform, related_name="uniforms", verbose_name=_('uniforms'))
    archived = models.BooleanField(default=False, verbose_name=_('archived'))
