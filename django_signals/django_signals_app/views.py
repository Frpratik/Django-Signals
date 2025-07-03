from django.http import JsonResponse
from .models import DemoModel
import threading

def signal_api(request):
    print("=== Before saving in API ===")
    print(f"View thread ID: {threading.get_ident()}")
    DemoModel.objects.create(name="Triggered by API")
    print("=== After saving in API ===")
    return JsonResponse({"message": "Check server logs!"})


""" 
Q.1
This simple API proves that Django signals are synchronous.

 How it works:
 1 When you call this API (by visiting /api/test-signal/),Django runs this view function.
 2 Inside the view, we save a DemoModel object.
 3 The post_save signal automatically runs immediately after the model is saved.
 4 The signal does a time.sleep(3) to simulate some work.
 5 The line "After saving in API" will not run until the signal finishes.

   So if you check your server log,
   you'll see that the signal runs BEFORE the "After saving" line prints.
    
 -> This proves that Django signals are synchronous by default.
"""


"""
Q.2
This API demonstrates whether Django signals run in the same thread as the caller.

How it works:
1. When you call this API endpoint (/api/test-signal/), it prints the thread ID of the view (caller).
2. The view saves a model instance, which triggers a signal.
3. The signal handler prints its own thread ID.
4. If both thread IDs are the same, it confirms that Django signals run in the same thread by default.

Check your server logs for the output.

o/p -> 
=== Before saving in API ===
View thread ID: 9504
=== Signal started ===
Signal thread ID: 9504
=== Signal finished ===
=== After saving in API ===

So, see in above op we are getting a same id(9504).
"""
