# Generated by Django 3.2.13 on 2022-11-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Where_is_teacher', '0005_remove_teacher_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'なし'), (1, '学科別'), (2, '五十音')], default=0, verbose_name='state')),
            ],
        ),
    ]
