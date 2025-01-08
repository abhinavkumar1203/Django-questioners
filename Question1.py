# When a signal is sent, the corresponding signal receiver executes immediately within the same thread and process as the sender. 

#Explaination by a simple code snippet : 

import time
from django.db.models.signals import post_save #Import the signal triggered after save() method is called
from django.dispatch import receiver #Establishes the connection of a function to signal
from django.contrib.auth.models import User

#Connect the post_save signal to the _handler function for the User model
@receiver(post_save, sender=User)
def _handler(sender, instance, **kwargs):
    #when a User instance is saved it is being executed with the help of Signal Handler
    # Upon calling the save() method, function gets triggered automatically
    print(f"Handler started for User: {instance.username}") # signal handling initialization
    time.sleep(5) # Prolonged time of execution to show synchronous behavior
    print(f"Handler completed for User: {instance.username}") #signal handling ends

if __name__ == "__main__":
    user = User(username="test_user")
    user.save()  

    # This line will only execute after the signal handler (_handler) completes,
    # proving that the signal execution is synchronous.
    print("User save completed")
