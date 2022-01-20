from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

# Create your views here.

def main(request):
    return render(request, 'kpop/main.html')

def kpop(request):
    kpop = models.Kpop.objects.all()
    return render(request, 'kpop/kpop.html', {'kpop': kpop})

def idol(request, id):
    idol = get_object_or_404(models.Kpop, id = id)
    return render(request, 'kpop/idol.html', {'idol': idol})

def add_idol(request):
    if request.method == 'POST':
        form = forms.IdolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Idol add')
    else:
        form = forms.IdolForm()
    return render(request, 'kpop/add_idol.html', {'form': form})

def idol_update(request, id):
    idol_object = get_object_or_404(models.Kpop, id = id)
    if request.method == 'POST':
        form = forms.IdolForm(instance=idol_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('idol UPDATED')
    else:
        form = forms.IdolForm(instance=idol_object)
    return render(request, 'kpop/idol_update.html', {'form': form,'idol': idol_object})

def idol_delete(request, id):
    idol_object = get_object_or_404(models.Kpop, id=id)
    idol_object.delete()
    return HttpResponse("Idol Deleted")
