# Generated by Django 2.1.3 on 2019-04-25 04:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0004_auto_20190308_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
