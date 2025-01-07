# When a signal is sent, the corresponding signal receiver executes immediately within the same thread and process as the sender. 

#Explaination by a simple code snippet : 

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def _handler(sender, instance, **kwargs):
    print(f"Handler started for User: {instance.username}")
    time.sleep(5)  
    print(f"Handler completed for User: {instance.username}")

if __name__ == "__main__":
    user = User(username="test_user")
    user.save()  

    print("User save completed")
