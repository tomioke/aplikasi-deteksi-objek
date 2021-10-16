from django.shortcuts import render
from .forms import ImageUpoadForm
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Create your views here.

def handle_upload_file(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home(request): # Fungsi halaman home
    return render(request, 'home.html')

def imageprocess(request):
    form = ImageUpoadForm(request.POST, request.FILES)
    if form.is_valid:
        handle_upload_file(request.FILES['image'])
        
        model = ResNet50(weights='imagenet')
        gambar = 'img.jpg'
        
        img = image.load_img(gambar, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        preds = model.predict(x)
        print('Predicted:', decode_predictions(preds, top=3)[0])
        
        # Tampilkan pada halaman html
        html = decode_predictions(preds, top=3)[0]
        res = []
        for e in html:
            res.append((e[1], np.round(e[2]*100,2)))
        return render(request, 'result.html', {'res': res})
        
    return render(request, 'result.html')

# Simpan hasil proses training 
