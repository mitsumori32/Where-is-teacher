# Generated by Django 3.2.13 on 2022-11-02 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('text', models.TextField(max_length=1000, verbose_name='comment')),
                ('time', models.DateTimeField(verbose_name='update time')),
                ('state', models.IntegerField(choices=[(0, '不明'), (1, '在室'), (2, '不在')], verbose_name='state')),
            ],
        ),
    ]
