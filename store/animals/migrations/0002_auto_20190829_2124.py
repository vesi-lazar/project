# Generated by Django 2.2.4 on 2019-08-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
