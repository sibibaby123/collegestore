# Generated by Django 4.2.6 on 2023-11-10 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_alter_collegepart_name_alter_collegepart_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authentication.department'),
        ),
    ]
