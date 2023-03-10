# Generated by Django 4.1.5 on 2023-01-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('order_amount', models.DecimalField(decimal_places=10, max_digits=10)),
                ('customer_name', models.CharField(max_length=200)),
                ('payment_url', models.CharField(blank=True, max_length=200)),
                ('payment_status', models.CharField(blank=True, choices=[('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('', '')], max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
