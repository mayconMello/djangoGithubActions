"""djangoGithubActions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import json

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from core import urls as core_urls


@csrf_exempt
@require_POST
def receiver_webhooks(request):
    payload = json.loads(request.body)

    print(payload)

    return HttpResponse()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include(core_urls)),
    path('hooks/', receiver_webhooks)
]
