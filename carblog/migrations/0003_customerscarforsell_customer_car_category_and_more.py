# Generated by Django 4.0.3 on 2022-09-18 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carblog', '0002_customerscarforsell_customer_car_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerscarforsell',
            name='customer_car_category',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='customerscarforsell',
            name='customer_car_price',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='ownsellcars',
            name='category',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='ownsellcars',
            name='price',
            field=models.CharField(default='', max_length=200),
        ),
    ]
