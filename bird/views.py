from django.shortcuts import render,redirect
from .models import Bird

# Create your views here.
def home(request):
    input=Bird.objects.all()
    context={'input':input}
    return render(request,'birdhome.html',context)

def create(request):
    if request.method == "POST":
        bn=request.POST.get('bname')
        bf=request.POST.get('bfood')
        bsn=request.POST.get('bScientificName')
        bh=request.POST.get('bHabitat')
        bmp=request.POST.get('bMigrationPattern')
        # bi=request.FILES.get('bimg')
        # bd=request.POST.get('bDateAdded')


        Bird.objects.create(
            bname=bn,
            bfood=bf,
            bScientificName=bsn,
            bHabitat=bh,
            bMigrationPattern=bmp,
            # bimg=bi,
            # bDateAdded=bd,
        )
        return redirect('birdhome')

    return render (request,'createbd.html')

def updatebd(request,pk):
    input=Bird.objects.get(id=pk)

    if request.method == "POST":
        bn=request.POST.get('bname')
        bf=request.POST.get('bfood')
        bsn=request.POST.get('bScientificName')
        bh=request.POST.get('bHabitat')
        bmp=request.POST.get('bMigrationPattern')
        # bi=request.FILES.get('bimg')
        # bd=request.POST.get(' bDateAdded')

        input.bname=bn,
        input.bfood=bf,
        input.bScientificName=bsn,
        input.bHabitat=bh,
        input.bMigrationPattern=bmp,
        # input.bimg=bi,
        # input.bDateAdded=bd
        input.save()
        return redirect('birdhome')
    
    context={'input':input}
    return render (request,'updatebd.html',context)

def deletebd(request,pk):
    data=Bird.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('birdhome')
    return render(request,'deletebd.html')