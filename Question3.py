# If the database operation is within a transaction Django signals run in the same database transaction as the caller

#Explaination by a simple code snippet : 

from django.db import models, transaction #Import transaction management tools
from django.db.models.signals import post_save
from django.dispatch import receiver

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def post_save_handler(sender, instance, **kwargs):
    print("Signal handler executed")
    TestModel.objects.create(name="Created from signal")

if __name__ == "__main__":
    #Main block to simulate save a TestModel instance and explain that signal handlers run in the same transaction as the caller.
    try:
        #Initialize an atomic transaction block
        with transaction.atomic():
            #Create a TestModel instance
            obj = TestModel(name="Main object")
            obj.save()  # Triggers the post_save signal

            #Raise an exception to simulate an error, causing a transaction rollback
            raise Exception("Simulating an error")
    except Exception as e:
        # Catch the exception and print a message indicating that the transaction was rolled back
        print(f"Transaction rolled back: {e}")

    print(f"Objects in DB: {TestModel.objects.all().count()}")
# If the signal and caller run in the same transaction, no objects should exist in the database because the transaction was rolled back.
