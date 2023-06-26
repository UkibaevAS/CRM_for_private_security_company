# Generated by Django 4.2.2 on 2023-06-26 17:47

from django.db import migrations, models
import gun.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='name')),
                ('description', models.CharField(db_index=True, max_length=100, verbose_name='description')),
                ('factory_number', models.CharField(db_index=True, max_length=15, verbose_name='factory_number')),
                ('certificate', models.ImageField(blank=True, null=True, upload_to=gun.models.certificate_directory_path, verbose_name='certificate')),
                ('date_test_shoot', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='date_test_shoot')),
                ('receipt_date', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='receipt_date')),
            ],
            options={
                'verbose_name': 'Gun',
                'verbose_name_plural': 'Guns',
            },
        ),
    ]
