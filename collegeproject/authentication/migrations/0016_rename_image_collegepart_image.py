# Generated by Django 4.2.6 on 2023-11-10 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_remove_purpose_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collegepart',
            old_name='Image',
            new_name='image',
        ),
    ]
