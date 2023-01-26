from django.db import models

# Create your models here.


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=200)
    order_amount = models.DecimalField(
        blank=False, decimal_places=1, max_digits=10)
    customer_name = models.CharField(max_length=200)
    payment_url = models.CharField(max_length=200, blank=True)
    payment_success_url = models.CharField(max_length=200, blank=True)
    payment_failure_url = models.CharField(max_length=200, blank=True)
    payment_status = models.CharField(max_length=50, blank=True, choices=[
                                      ('SUCCESS', 'Success'), ('FAILURE', 'Failure')])
    isPaid = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str('Order for ' + str(self.customer_name))

    
