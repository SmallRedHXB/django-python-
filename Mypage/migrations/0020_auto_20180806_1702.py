# Generated by Django 2.0.5 on 2018-08-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mypage', '0019_params_param'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='params',
            name='id',
        ),
        migrations.AlterField(
            model_name='params',
            name='param',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]