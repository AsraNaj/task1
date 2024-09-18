
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received")
    time.sleep(5)  # Simulate a delay
    print("Signal handling completed")
# views.py
from .models import MyModel

def my_view(request):
    MyModel.objects.create(name='example')
    print("Model instance created")
