# Generated by Django 4.2.6 on 2023-11-10 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0020_alter_userorder_depart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='depart',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.department'),
        ),
    ]
