# Generated by Django 2.2.6 on 2019-11-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0007_guilde_str_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='str_slug',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]