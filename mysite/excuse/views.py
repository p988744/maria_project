from django.shortcuts import render
from django.http import HttpResponse
import random
from excuse.models import Excuse

# Create your views here.

def home(request):
    excuse = random.choice(Excuse.objects.all())
    return render(request, "index.html", {'excuse': excuse})
