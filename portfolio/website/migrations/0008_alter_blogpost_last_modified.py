# Generated by Django 5.0.1 on 2024-02-20 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_blogpost_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='last_modified',
            field=models.DateField(),
        ),
    ]
