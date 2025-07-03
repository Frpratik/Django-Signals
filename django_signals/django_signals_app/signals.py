from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DemoModel

import time
import threading  # We have imported threding to get ID number of current thred.

@receiver(post_save, sender=DemoModel)
def my_signal(sender, instance, **kwargs):
    print("=== Signal started ===")
    print(f"Signal thread ID: {threading.get_ident()}") 
    time.sleep(2)
    print("=== Signal finished ===")
