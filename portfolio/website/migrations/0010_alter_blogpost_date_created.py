# Generated by Django 5.0.1 on 2024-02-20 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_blogpost_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]