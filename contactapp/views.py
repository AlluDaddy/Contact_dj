from django.shortcuts import render, redirect
from .models import Contact

def index(request):
    data = Contact.objects.all()
    return render(request,"index.html",{ "data" : data})   

def profile_id(request, my_id):
    identity = Contact.objects.get(id=my_id)
    return render(request,"contact-profile.html",{"id":identity})


def profile(request):
    if request.method =="POST":
        full_name = request.POST["fullname"]
        relation = request.POST["relation"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        data = Contact(full_name=full_name, relation=relation, email=email, phone=phone, address=address)
        data.save()
        return redirect('index')
    return render(request,"contact-profile.html")
  

def edit(request):
    return render(request,"edit.html")

def edit_id(request, my_id):
    identity = Contact.objects.get(id=my_id)
    if request.method =="POST":
        identity.full_name = request.POST["fullname"]
        identity.relation = request.POST["relation"]
        identity.email = request.POST["email"]
        identity.phone = request.POST["phone"]
        identity.address = request.POST["address"]
        identity.save()
        return redirect('index')
    return render(request,"editid.html",{'id':identity})

def dlt_id(request,my_id):
    identity = Contact.objects.get(id=my_id)
    return render(request,"dlt.html",{"id":identity})

def confirm_id(request,my_id):
    identity = Contact.objects.get(id=my_id)
    identity.delete()
    return redirect("index")
    
