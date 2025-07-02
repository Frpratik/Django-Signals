from django.http import JsonResponse
from .models import DemoModel

def signal_api(request):
    print("=== Before saving in API ===")
    DemoModel.objects.create(name="Triggered by API")
    print("=== After saving in API ===")
    return JsonResponse({"message": "Check server logs!"})


""" 
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