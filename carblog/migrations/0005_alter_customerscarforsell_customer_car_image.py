# Generated by Django 4.0.3 on 2022-09-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carblog', '0004_alter_customerscarforsell_customer_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerscarforsell',
            name='customer_car_image',
            field=models.ImageField(blank=True, null=True, upload_to='Media/customercar/'),
        ),
    ]