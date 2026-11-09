Nama: Hadyasalha Alina Anindya
NPM: 2506620406
Kelas: PBP A

#Tugas 1
Pertanyaan Refleksif
1. Pada portofolio saya, saya hanya menggunakan <div> dan tidak menggunakan elemen semantik HTML5 karena design yang saya buat masih sederhana.
2. Tata letak section baru dan 2 image yang digabung. Saya mengevaluasi posisi secara coba-coba dengan menjalankan website tiap edit
3. Saya ingin section yang dibuat ada pada laman berbeda. Website saya hanya ada 1 halaman sehingga gambaran statis dan tidak ada interaksi

Penggunaan AI: https://chatgpt.com/share/6a9eeade-aa20-83ec-b53c-6387d132ac1f

#Tugas 2
1. Saat user pertama kali membuka django, request tersebut diteruskan ke urls.py proyek lalu ke urls.py aplikasi. URL tersebut menentukan view yang akan ditampilkan. Lalu, view memproses request dan melanjutkannya ke model kemudian baru dikirim ke template. Misalnya, request ke section education, model akan mengambil education.html. Template mengubah data jadi html dan django meneruskannya kembali ke browser untuk ditampilkan.

2. Data bagian portofolio sebaiknya disimpan di model agar pemeliharaan dan pengembangan aplikasi lebih efisien. Jika ingin menggunakan data portofolio di section lain atau mengeditnya, bisa langsung ubah di model tanpa harus mengubah satu persatu di template. Serta, jika ingin menggunakan data yang sama atu ada kesalahan dalam penggunaan data tersebut bisa tau sumber awalnya darimana tanpa perlu mencari di template. Hanya perlu "memanggil" model untuk kode-kode seterusnya.

3. makemigrations: membuat file migration untuk mencatat perubahan model
migrate: menerapkan model yang diubah
contoh: buat model baru yaitu education. Jalankan dulu makemigrations untuk mengubah modelnya lalu diterapkan saat migrate agar bisa ditambahkan ke database.

Penggunaan AI:
Menggunakan AI untuk push data di section ke PWS (code di terminal lokal dan PWS)
https://chatgpt.com/s/t_6aa81b8648488191b2c13432f4b4ae96

#Tugas 3
1. Penggunaan ModelForm membuat pembuatan form model django jadi otomatis, jadi tidak perlu membuat setiap field secara manual di HTML. Penggunaan ModelForm juga dapat menghubungkan bdata sehingga pengerjaan lebih praktis dan mengurangi kemungkinan kesalahan.

{% csrf_token %} memastikan request yang dikirim berasal dari aplikasi lokal bukan pihak lain.

2. JSON lebih ringkas dan mudah dibaca daripada XML.

3. Browser mengirim request http ke url tertentu. Lalu, urls.py mencocokan dengan request yang dikirim ke view yang sesuai. View mengambil data dari folder portofolio dengan model django. Data dari model django dikirim sebagai json, makanya diperlukan serialization, untuk mengubah jdon menjadi dictionary. Setelah serialization, data dikirim ke browser (berbentuk json) dan memproses data untuk ditampilkan.

#Tugas 4

#Tugas 5
Tidak menggunakan AI, hanya mengikuti template

1. Debouncing = teknik menunda eksekusi fungsi sampai user berhenti mengetik sampai waktu tertentu. Digunakan agar program tidak terus berjalan tiap user mengetik, baru jalan saatuser selesai sehingga lebih efisien dan tidak memberatkan server.

2. Untuk menunggu proses request selesai sebelum kode lanjut ke baris selanjutnya. Jika tidak menggunakan await, hasil fetch() masih berupa Promise, jadi daya response belum bisa digunakan dan bisa error.

3. Attack dengan memasukan script berbahaya ke halaman web. Data yang ditampilkan melalui ajax/javascript lebih rentan karena developer bisa memasukannya langsung ke DOM. Django template secara default menggunakan auto-escaping.

#Tugas 6
1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!
>> REST = Representational State Transfer, gaya arsitektur API yang mengatur komunikasi antara client dan server menggunakan HTTP methods dan resource melalui URL. Mengembalikan JSON saja belum cukup disebut RESTful karena JSON hanya format pertukaran data. API juga harus mengikuti prinsip REST, seperti stateless, penggunaan HTTP methods yang tepat, dan struktur resource yang jelas.
>> PUT Vs PATCH
>> PUT = Mengganti keseluruhan data resource
>> PATCH = Mengubah sebagian data resource

2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?
>> Berfungsi mengubah objek Django Model menjadi format JSON dan sebaliknya, serta melakukan validasi data.
>> Keuntungannya, yaitu konversi data lebih mudah, memiliki validasi data, mengurangi penulisan dictionary secara manual.

3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?
>> Autentikasi (Authentication): Proses memverifikasi identitas pengguna. Contoh: login menggunakan username dan password.
>> Otorisasi (Authorization): Proses menentukan hak akses pengguna. Contoh: admin boleh menghapus data, sedangkan user biasa tidak.

4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?
>> Pada SessionAuthentication, browser mengirimkan session cookie secara otomatis. Oleh karena itu, request yang mengubah data (POST, PUT, PATCH, DELETE) memerlukan token CSRF untuk memastikan request berasal dari sumber yang memiliki token valid.
>> force_authenticate tidak cukup untuk menguji CSRF karena melewati proses autentikasi normal, sehingga pemeriksaan CSRF oleh SessionAuthentication tidak benar-benar diuji.