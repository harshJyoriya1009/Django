from django.shortcuts import render
from .models import AppVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_app1(request):
    apps= AppVarity.objects.all()
    return render( request, 'app1/all_app1.html', {'apps': apps})

def app1_detail(request, app1_id):
    app1 = get_object_or_404(AppVarity, pk = app1_id)
    return render(request, 'app1/app1_detail.html', {'app1': app1}) 
    
