# Generated by Django 4.2.2 on 2023-07-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Briefing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='name')),
                ('description', models.TextField(db_index=True, verbose_name='description')),
                ('data_briefing', models.CharField(db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, verbose_name='data')),
                ('committee_chair', models.CharField(db_index=True, max_length=30, verbose_name='committee_chair')),
                ('data_next_briefing', models.CharField(db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, verbose_name='data_next')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='name')),
                ('series_and_number', models.CharField(db_index=True, help_text='format: series number', max_length=30, verbose_name='series_and_number')),
                ('date_issue', models.CharField(db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, verbose_name='date_issue')),
                ('date_expiration', models.CharField(blank=True, db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, null=True, verbose_name='date_expiration')),
                ('who_issued', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='who_issued')),
                ('place_registration', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='place_registration')),
                ('driving_license_categories', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='driving_license_categorie')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
    ]
