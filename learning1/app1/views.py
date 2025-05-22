from django.shortcuts import render
from .models import AppVarity, Store
from django.shortcuts import get_object_or_404
from .forms import AppVarityForm

# Create your views here.
def all_app1(request):
    apps= AppVarity.objects.all()
    return render( request, 'app1/all_app1.html', {'apps': apps})

def app1_detail(request, app1_id):
    app1 = get_object_or_404(AppVarity, pk = app1_id)
    return render(request, 'app1/app1_detail.html', {'app1': app1}) 

def app_store_view(request):
    stores = None
    if request.method == 'POST':
        form = AppVarityForm(request.POST)
        if form.is_valid():
            app_variety = form.cleaned_data['app_varity']
            stores = Store.objects.filter(app_varities = app_variety) 

    else:
        form = AppVarityForm()
             
    return render(request, 'app1/app_stores.html', {'stores': stores, 'form': form})
    
