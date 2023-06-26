from django.db import models
from django.utils.translation import gettext_lazy as _

def briefing_report_directory_path(instance: "Briefing", filename: str) -> str:
    return "briefing/briefing_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Briefing(models.Model):


    name = models.CharField(max_length=30, db_index=True, verbose_name=_('name'))
    description = models.TextField(null=False, blank=False, db_index=True, verbose_name=_('description'))
    data_briefing = models.CharField(max_length=10, null=False, blank=False, db_index=True, help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data_briefing'))
    committee_chair = models.CharField(max_length=30, null=False, blank=False, db_index=True, verbose_name=_('committee_chair'))
    briefing_report =  models.ImageField(null=True, blank=True, upload_to=briefing_report_directory_path, verbose_name=_('preview'))
    data_next_briefing = models.CharField(max_length=10, null=False, blank=False, db_index=True, help_text=_("format data: dd.mm.yyyy"), verbose_name=_('data_briefing'))

    def __str__(self):
        return f"{_('Briefing')}(pk={self.pk}, name={self.name!r})"
