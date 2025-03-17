from django.shortcuts import render,redirect
from .models import Animal

# Create your views here.
def anihome(request):
    data=Animal.objects.all()
    context={'data':data}
    return render(request,'anihome.html',context)

def createani(request):
    if request.method == "POST":
        n=request.POST.get('name')
        at=request.POST.get('nimal_type')
        f=request.POST.get('food')
        h=request.POST.get('habitat')
        c=request.POST.get('color')
        sa=request.POST.get('special_abilities')
        i=request.FILES.get('image')
        # ls=request.POST.get('alifespan')

        Animal.objects.create(
            aname=n,
            animal_type=at,
            afood=f,
            ahabitat=h,
            acolor=c,
            aspecial_abilities=sa,
            aimage=i,
            # alifespan=ls,
        )
        return redirect('anihome')  
    
    return render(request,'create.html')

# def updateani(request,pk):
#     data=Animal.objects.get(id=pk)

#     if request.method == "POST":
#         n=request.POST.get('name')
#         at=request.POST.get('animal_type ')
#         f=request.POST.get('food')
#         h=request.POST.get('ahabitat')
#         c=request.POST.get('color')
#         sa=request.POST.get('special_abilities')
#         i=request.FILES.get('image')
#         # ls=request.POST.get('alifespan')

#         data.aname=n,
#         data.animal_type=at,
#         data.afood=f,
#         data.ahabitat=h,
#         data.acolor=c,
#         data.aspecial_abilities=sa,
#         data.aimage=i,
#          # data.alifespan=ls,

#         if request.FILES.get('image'):
#             data.aimage = request.FILES.get('image')

       
#         data.save()
#         return redirect('anihome')
    
#     context={'data':data}
#     return render(request,'update.html',context)


def updateani(request, pk):
    data = Animal.objects.get(id=pk)

    if request.method == "POST":
        data.aname = request.POST.get('name')
        data.animal_type = request.POST.get('animal_type')  # Fix: Removed space
        data.afood = request.POST.get('food')
        data.ahabitat = request.POST.get('ahabitat')
        data.acolor = request.POST.get('color')
        data.aspecial_abilities = request.POST.get('special_abilities')

        # Handling image update properly
        if request.FILES.get('image'):
            data.aimage = request.FILES.get('image')

        data.save()  # Ensure you save the object correctly
        return redirect('anihome')

    context = {'data': data}
    return render(request, 'update.html', context)




def deleteani(request,pk):
    data=Animal.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('anihome')
    return render(request,'delete.html')