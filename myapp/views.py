from django.shortcuts import render
from django.http import HttpResponse
from .models import People, MyModel
# Create your views here.

def people(request):
    people_list = People.objects.all()
    context = {
        "people_list": people_list,
    }
    return render(request, "index.html", context)

def new_person(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        joined_date = request.POST.get("joined_date")

        new_person = People(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            joined_date=joined_date
        )
        new_person.save()
        return HttpResponse("New person added successfully.")
    else:
        return render(request, "new_person.html")