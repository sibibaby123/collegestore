# Generated by Django 4.2.6 on 2023-11-10 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_remove_userorder_depart_userorder_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userorder',
            old_name='purpose',
            new_name='keyu',
        ),
    ]
