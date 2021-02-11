# Generated by Django 3.1.6 on 2021-02-11 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210211_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
