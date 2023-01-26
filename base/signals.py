from django.db.models.signals import pre_save,post_save
from base.models import *

def updatePayment(sender , instance, **kwargs):
    if str(instance.payment_status).upper() == 'SUCCESS':
        instance.isPaid = True
        print('Payment Successful!')
    
    if str(instance.payment_status).upper() == 'FAILURE':
        instance.isPaid = False
        print('Payment Failed!')

pre_save.connect(updatePayment, Order)
    

