# Generated by Django 4.1 on 2022-08-21 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_etl', '0002_censusetl_capital_gain_censusetl_capital_loss_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='censusetl',
            old_name='eduction',
            new_name='education',
        ),
    ]
