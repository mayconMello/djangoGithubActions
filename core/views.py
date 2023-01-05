from django.forms import model_to_dict
from django.http import JsonResponse

from core.models import Contact


# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()

    data = [
        model_to_dict(contact)
        for contact in contacts
    ]

    return JsonResponse(data, safe=False)
