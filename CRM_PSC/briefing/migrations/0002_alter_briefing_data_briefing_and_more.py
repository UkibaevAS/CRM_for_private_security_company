# Generated by Django 4.2.2 on 2023-06-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='briefing',
            name='data_briefing',
            field=models.CharField(db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, verbose_name='data_briefing'),
        ),
        migrations.AlterField(
            model_name='briefing',
            name='data_next_briefing',
            field=models.CharField(db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, verbose_name='data_briefing'),
        ),
    ]
