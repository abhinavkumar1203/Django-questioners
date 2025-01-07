# If the database operation is within a transaction Django signals run in the same database transaction as the caller

#Explaination by a simple code snippet : 

from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def post_save_handler(sender, instance, **kwargs):
    print("Signal handler executed")
    TestModel.objects.create(name="Created from signal")

if __name__ == "__main__":
    try:
        with transaction.atomic():
            obj = TestModel(name="Main object")
            obj.save()  
            
            raise Exception("Simulating an error")
    except Exception as e:
        print(f"Transaction rolled back: {e}")

    print(f"Objects in DB: {TestModel.objects.all().count()}")
