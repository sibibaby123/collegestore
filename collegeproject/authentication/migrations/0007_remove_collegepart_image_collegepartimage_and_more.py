# Generated by Django 4.2.6 on 2023-10-18 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_collegepart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegepart',
            name='image',
        ),
        migrations.CreateModel(
            name='CollegepartImage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(upload_to='collegepart')),
                ('collegepart', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authentication.collegepart')),
            ],
        ),
        migrations.AddField(
            model_name='collegepart',
            name='Image',
            field=models.ImageField(default=-2015, upload_to='collegepart'),
            preserve_default=False,
        ),
    ]
