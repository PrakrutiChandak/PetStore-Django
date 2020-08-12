# Generated by Django 3.1 on 2020-08-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('submitter', models.CharField(max_length=80)),
                ('species', models.CharField(max_length=80)),
                ('breed', models.CharField(blank=True, max_length=80)),
                ('description', models.TextField()),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('submission_date', models.DateField()),
                ('age', models.IntegerField(null=True)),
                ('vaccinations', models.ManyToManyField(blank=True, to='adoptions.Vaccine')),
            ],
        ),
    ]
