from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import Affiliated_company, Department, Position
from document.models import Document, Briefing
from equipment.models import Uniform

def photo_directory_path(instance: "Worker", filename: str) -> str:
    return "Worker/photo/{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Worker(models.Model):
    class Meta:
        verbose_name = _('Worker')
        verbose_name_plural = _('Workers')

    first_name = models.CharField(max_length=30, db_index=True, verbose_name=_('first_name'))
    middle_name = models.CharField(max_length=30, db_index=True, verbose_name=_('middle_name'))
    second_name = models.CharField(max_length=50, db_index=True, verbose_name=_('second_name'))
    photo = models.ImageField(null=True, blank=True, upload_to=photo_directory_path)
    phone = models.PositiveBigIntegerField(default=0, null=True, blank=True, db_index=True,
                                           help_text=_("format phone: 83517772233"), verbose_name=_('phone'))
    address = models.CharField(max_length=150, null=False, blank=False, db_index=True, verbose_name=_('address'))
    date_birth = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                  help_text=_("format data: dd.mm.yyyy"), verbose_name=_('date_birth'))
    data_employment = models.CharField(max_length=10, null=False, blank=False, db_index=True,
                                       help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data_employment'))
    organization = models.ForeignKey(Affiliated_company, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
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

