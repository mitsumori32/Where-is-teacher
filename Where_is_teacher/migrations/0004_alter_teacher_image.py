# Generated by Django 3.2.13 on 2022-11-09 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Where_is_teacher', '0003_auto_20221109_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='masuyama.jpg', upload_to='static/Where_is_teacher/images'),
        ),
    ]
