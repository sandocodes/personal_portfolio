# Generated by Django 5.0.1 on 2024-02-20 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]