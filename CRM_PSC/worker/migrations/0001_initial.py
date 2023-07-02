# Generated by Django 4.2.2 on 2023-07-02 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0001_initial'),
        ('document', '0001_initial'),
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=30, verbose_name='first_name')),
                ('second_name', models.CharField(db_index=True, max_length=50, verbose_name='second_name')),
                ('middle_name', models.CharField(db_index=True, max_length=30, verbose_name='middle_name')),
                ('phone', models.PositiveBigIntegerField(blank=True, db_index=True, default=0, help_text='format phone: 83517772233', null=True, verbose_name='phone')),
                ('address', models.CharField(db_index=True, max_length=150, verbose_name='address')),
                ('date_birth', models.CharField(db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, verbose_name='date_birth')),
                ('data_employment', models.CharField(db_index=True, help_text='format data: dd.mm.yyyy', max_length=10, verbose_name='data_employment')),
                ('category', models.SmallIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='category')),
                ('electrical_safety_qualification', models.SmallIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='electrical_safety_qualification')),
                ('size_shoe', models.SmallIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='size_shoe')),
                ('size_clothing', models.SmallIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='size_clothing')),
                ('size_hat', models.SmallIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='size_hat')),
                ('archived', models.BooleanField(default=False, verbose_name='archived')),
                ('briefings', models.ManyToManyField(related_name='briefings', to='document.briefing', verbose_name='briefings')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='config.department')),
                ('documents', models.ManyToManyField(related_name='documents', to='document.document', verbose_name='documents')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='config.affiliated_company')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='config.position')),
                ('uniforms', models.ManyToManyField(related_name='uniforms', to='equipment.uniform', verbose_name='uniforms')),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
    ]
