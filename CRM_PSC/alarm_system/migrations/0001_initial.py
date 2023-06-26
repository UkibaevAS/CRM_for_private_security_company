# Generated by Django 4.2.2 on 2023-06-26 18:14

import alarm_system.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm_system',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='name')),
                ('description', models.CharField(db_index=True, max_length=100, verbose_name='description')),
                ('factory_number', models.CharField(db_index=True, max_length=15, verbose_name='factory_number')),
                ('certificate', models.ImageField(blank=True, null=True, upload_to=alarm_system.models.certificate_directory_path, verbose_name='certificate')),
                ('installation_date', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='installation_date')),
                ('maintenance_interval', models.CharField(db_index=True, max_length=15, verbose_name='maintenance_interval')),
                ('date_manufacture', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='date_manufacture')),
                ('receipt_date', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='receipt_date')),
                ('service_date', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='service_date')),
                ('service_date_next', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='service_date')),
                ('maintenance_report', models.ImageField(blank=True, null=True, upload_to=alarm_system.models.maintenance_report_directory_path, verbose_name='certificate')),
            ],
            options={
                'verbose_name': 'Alarm_system',
                'verbose_name_plural': 'Alarm_systems',
            },
        ),
    ]
