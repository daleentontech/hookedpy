
import json
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import View
from django.conf import settings

from django.http import HttpResponse

from braces.views import CsrfExemptMixin

class ProcessHookView(CsrfExemptMixin, View):
    """
    Process the hook request.
    """
    def post(self, request, *args, **kwargs):
        """
        This view will recieve an event on the url you created
        and process the event however you wish to do it.
        It is expected that the url be provided to the source.

        :- source is whoever will be sending you webhook events
        """
        try:
            data = json.loads(request.body)
            print(data)
        except Exception: #ideally you should handle this better
            return HttpResponse("Error while processing event", status=400)
        return HttpResponse(data, status=status.HTTP_201_CREATED)

class SendWebhookView(CsrfExemptMixin, View):
    """
    This view will send a webhook event to the url you recieved
    from the destination and process the event however you wish to do it.
    
    :- destination is whoever you will be sending webhook events
    """
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(data)
        except Exception:
            return HttpResponse("status=status.HTTP_400_BAD_REQUEST")
        return HttpResponse("status=status.HTTP_200_OK")