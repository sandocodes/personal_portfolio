# Generated by Django 5.0.1 on 2024-02-20 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_blogpost_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
