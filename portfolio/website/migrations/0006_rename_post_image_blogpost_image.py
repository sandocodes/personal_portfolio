# Generated by Django 5.0.1 on 2024-02-20 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_blogpost_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='post_image',
            new_name='image',
        ),
    ]