# Generated by Django 4.1.5 on 2023-01-25 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_order_payment_status_alter_order_order_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.order'),
        ),
    ]
