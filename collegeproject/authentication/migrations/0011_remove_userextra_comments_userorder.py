# Generated by Django 4.2.6 on 2023-11-06 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0010_alter_purpose_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextra',
            name='comments',
        ),
        migrations.CreateModel(
            name='Userorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=200)),
                ('item_pen', models.CharField(max_length=20, null=True)),
                ('item_pen_no', models.IntegerField()),
                ('item_book', models.CharField(max_length=20, null=True)),
                ('item_book_no', models.IntegerField()),
                ('item_paper', models.CharField(max_length=20, null=True)),
                ('item_paper_no', models.IntegerField()),
                ('checkedin', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
