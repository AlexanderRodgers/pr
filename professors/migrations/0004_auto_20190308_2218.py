# Generated by Django 2.1.3 on 2019-03-09 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0003_auto_20190307_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='professors.Major'),
        ),
    ]
