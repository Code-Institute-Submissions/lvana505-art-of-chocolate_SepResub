# Generated by Django 3.2 on 2022-09-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20220919_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
