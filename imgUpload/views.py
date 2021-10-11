from django.shortcuts import render
from .forms import ImageUpoadForm

# Create your views here.
def home(request): # Fungsi halaman home
    return render(request, 'home.html')

def imageprocess(request):
    form = ImageUpoadForm(request.POST, request.FILES)
    if form.is_valid:
        handle_upload_file(request.FILES['image'])
    return render(request, 'result.html')

# Simpan hasil proses training 
def handle_upload_file(f):
    with open(img.jpg, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)