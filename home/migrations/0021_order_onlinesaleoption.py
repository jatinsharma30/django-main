# Generated by Django 3.2.8 on 2022-02-27 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20220228_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='onlineSaleOption',
            field=models.CharField(blank=True, choices=[('Swiggy', 'Swiggy'), ('Zomato', 'Zomato')], max_length=6, null=True),
        ),
    ]
