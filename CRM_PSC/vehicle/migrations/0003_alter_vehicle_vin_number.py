# Generated by Django 4.2.2 on 2023-06-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_alter_vehicle_passport_copy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='VIN_number',
            field=models.CharField(db_index=True, max_length=20, verbose_name='VIN_number'),
        ),
    ]
