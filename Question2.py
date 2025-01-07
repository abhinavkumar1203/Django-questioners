# Yes, Django signals run in the same thread as the caller by default which means when a signal is sent,
# the signal handler executes within the same thread as the code that triggered the signal.

#Explaination by a simple code snippet : 

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_post_save_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

if __name__ == "__main__":
    print(f"Caller thread: {threading.current_thread().name}")

    user = User(username="test_user")
    user.save() 


