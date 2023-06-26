# Generated by Django 4.2.2 on 2023-06-26 16:32

import armor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=15, verbose_name='name')),
                ('description', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='description')),
                ('factory_number', models.CharField(blank=True, db_index=True, max_length=15, null=True, verbose_name='factory_number')),
                ('date_manufacture', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='date_manufacture')),
                ('protection_category', models.SmallIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='protection_category')),
                ('date_purchase', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='date_purchase')),
                ('certificate', models.ImageField(blank=True, null=True, upload_to=armor.models.certificate_directory_path, verbose_name='foto')),
            ],
            options={
                'verbose_name': 'Armor',
                'verbose_name_plural': 'Armors',
            },
        ),
    ]