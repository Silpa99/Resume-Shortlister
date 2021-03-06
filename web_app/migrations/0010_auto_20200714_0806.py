# Generated by Django 2.2.14 on 2020-07-14 02:36

from django.db import migrations, models
import django.utils.timezone
import web_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_merge_20200713_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AlterModelManagers(
            name='profile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_postings',
            name='company',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='job_postings',
            name='job_address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='upload_your_resume',
            field=models.FileField(null=True, upload_to=web_app.models.user_directory_path),
        ),
    ]
