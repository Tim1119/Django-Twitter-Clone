# Generated by Django 3.1.1 on 2020-12-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0004_auto_20201216_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
