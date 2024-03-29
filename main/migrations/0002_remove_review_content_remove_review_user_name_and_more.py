# Generated by Django 4.2.8 on 2024-03-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user_name',
        ),
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='review',
            name='nickname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='service',
            field=models.CharField(default='', max_length=100),
        ),
    ]
