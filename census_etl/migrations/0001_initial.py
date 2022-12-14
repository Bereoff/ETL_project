# Generated by Django 4.1 on 2022-08-18 23:32

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CensusEtl',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)])),
                ('workclass', models.CharField(blank=True, max_length=80, null=True)),
                ('sex', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=10, null=True)),
            ],
        ),
    ]
