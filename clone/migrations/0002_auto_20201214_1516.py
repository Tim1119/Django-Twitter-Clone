# Generated by Django 3.1.1 on 2020-12-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
