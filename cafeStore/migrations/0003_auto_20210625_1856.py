# Generated by Django 3.2.4 on 2021-06-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeStore', '0002_auto_20210625_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafeproducts',
            name='category',
            field=models.CharField(choices=[('coffee_and_tea', 'COFFEE AND TEA'), ('beverages', 'BEVERAGES'), ('munchies', 'MUNCHIES'), ('desert', 'DESERT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='cafeproducts',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
