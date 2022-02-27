# Generated by Django 3.2.8 on 2022-02-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_expense_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Amazon Pay', 'Amazon Pay'), ('Google Pay', 'Google Pay'), ('PhonePe', 'PhonePe'), ('Paytm', 'Paytm'), ('Card', 'Card')], default='Cash', max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method2',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Amazon Pay', 'Amazon Pay'), ('Google Pay', 'Google Pay'), ('PhonePe', 'PhonePe'), ('Paytm', 'Paytm'), ('Card', 'Card')], max_length=15, null=True),
        ),
    ]
