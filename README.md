<!-- Istall Library -->
pip install -r requirements.txt
1. Django==1.11.17

<!-- A. Desain website dahulu -->

1. cd C:\Users\USER\My Project
2. django-admin.exe startproject objectDetection
3. type (dir), and search objectDetection
4. cd objectDetection
5. Run server : python manage.py runserver

6. Buat perintah baru unutk halaman upload gambar
python manage.py startapp imgUpload

7. Buat folder templates untuk halaman webnya

8. Di dalam folder templates buat halaman 'home.html', buat skrip html pertama
dan hubungkan pada folder objectDetection.

9. Dalam folder objectDetection kemudian masuk settings.py cari tulisan 'TEMPLATES' ctrl+F lalu isikan pada DIRS folder 'templates' seperti ini <!--'DIRS': ['templates'], -->

10. Masuk masih folder objectDetection kemudian masuk ke urls.py tambahkan skrip <!-- url(r'imgUpload', include('imgUpload.urls')), --> dibawah persis "urlpatterns" kemudian tambahkan "include" pada skrip <!-- from django.conf.urls import url, include -->

11. Kemudian pindah ke folder imgUpload buat new file kemudian kasih nama "urls.py" kemudian copy skrip pada file "urls.py" pada folder objectDetection

12. Pada urls.py folder imgUpload, hapus semua skrip pada variable urlpatterns kemudian ganti seperti ini <!-- url(r'^$', views.home, name='home'), --> dan tambahkan library dengan <!-- from . import views --> dibawah django.contrib

13. Kemudian masuk ke views.py pada folder imgUpload, dibawah tulisan create views here, ketik <!--def home(request):
    <!--return render(request, 'home.html')  -->

14. Tambahkan folder imgUpload pada setting.py di folder objectDetection kemudian cari "INSTALLED_APPS" lalu tambahkan skrip <!-- 'imgUpload', --> dibawah contrib.staticfiles

15. Test dengan halaman http://127.0.0.1:8000/imgUpload. maka akan muncul tulisan "This is my Pages" kalau hanya buka http://127.0.0.1:8000 akan muncul error karena belum buat halaman utamanya

<!-- Deploy project ke Heroku -->
1. Pastikan sudah membuat file requirements.text, runtime.txt, readme.md, setup.sh, ProcFile(khusus untuk deploy via heroku)

1. Isi skrip requirements.txt sesuaikan dengan library yang di pakai pada projek misalkan seperti ini:
Django==1.11.17
gunicorn==19.7.1
keras==2.6.0
tensorflow-gpu==1.15 # Ukuran file 486 mb :)
django_heroku
whitenoise

2. Isi skrip runtime.txt sesuaikan dengan versi python yang dipakai.
python-3.7.12

3. Isi skrip Procfile khusus Django berisi seperti berikut:
web: gunicorn "<nama_project>".wsgi --log-file -

4. Upload projek ke github, misalkan url projek https://github.com/tomioke/aplikasi-deteksi-objek.git

5. Masuk dan login heroku, setelah masuk ke waebsitenya pilih New pada pojok kanan atas, pilih create new app

6. Berikan judul aplikasinya misal deteksi-objek, biarkan saja country seperti itu lalu create apps

7. Hubungkan deployment ke github, login dan berikan akses lalu scroll bawah cari nama repositori misal aplikasi-deteksi-objek lalu klik connet, tunggu sebentar.

8. Jika sudah scrol ke bawah aktifkan automatic deploy, tidak usah di cetang, lalu kebawah pilih deploy branch, Tunggu sampai proses selesai.

9. Apabila sudah selesai bisa pilih Open apps lalu diarahkan ke halaman kita

<!-- Membuat backend dengan keras -->
1. Buka website https://keras.io/api/applications/, lalu pilih salah satu model. Disini untuk contoh akan menggunakan Resnet50 model.





