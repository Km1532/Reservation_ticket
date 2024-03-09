# Generated by Django 4.2.8 on 2024-03-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Користувач', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users_images', verbose_name='Аватарка'),
        ),
    ]
