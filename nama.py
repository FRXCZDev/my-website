import random

# Daftar nama depan yang modern dan populer di kalangan anak generasi Z di Indonesia
nama_depan = [
    "Blaise", "Cleo", "Dara", "Eli", "Faye", "Gus", "Hope", "Ira", "Jax", "Kade",
    "Lily", "Max", "Nell", "Oren", "Pax", "Reid", "Shay", "Tess", "Vera", "Wynn",
    "Xan", "Yara", "Zane",
    "Abimanyu", "Aditya", "Aldo", "Alif", "Arga", "Arjun", "Arya", "Azka", "Bima", "Bintang",
    "Cahya", "Damar", "Dhani", "Dimas", "Dio", "Eka", "Elang", "Fadhil", "Farhan", "Fikri",
    "Galih", "Gilang", "Hafiz", "Hanif", "Harun", "Hendra", "Iqbal", "Irfan", "Jaka", "Januar",
    "Khalid", "Luthfi", "Mahendra", "Malik", "Naufal", "Nugroho", "Oka", "Pradipta", "Putra", "Raka",
    "Rama", "Randy", "Rizky", "Roni", "Ryan", "Satria", "Seto", "Syahrul", "Teguh", "Tio",
    "Vikram", "Wahyu", "Yusuf", "Zaky", "Bagas", "Bayu", "Bram", "Candra", "Cipto", "Daffa",
    "Dani", "Daru", "Dede", "Doni", "Dwi", "Edo", "Evan", "Faisal", "Ferry", "Fikri",
    "Fitra", "Gani", "Gio", "Hadi", "Hafiz", "Halim", "Hanafi", "Haryo", "Ilham", "Indra",
    "Jefri", "Joko", "Kamal", "Kurniawan", "Laksamana", "Lanang", "Lucky", "Maulana", "Muhammad", "Nova",
    "Nugraha", "Omar", "Pandu", "Prasetya", "Putu", "Rahmat", "Ridwan", "Rizal", "Rizwan", "Salman",
    "Samsul", "Saputra", "Septian", "Sigit", "Taufik", "Teguh", "Teuku", "Tri", "Usman", "Vicky",
    "Wawan", "Wisnu", "Yayan", "Yoga", "Zul", "Ahmad", "Aji", "Akbar", "Andika", "Anto",
    "Ardi", "Ari", "Arif", "Bagus", "Bambang", "Budi", "Dani", "Dedi", "Denny", "Dewi",
    "Edi", "Eko", "Fajar", "Ferry", "Fitria", "Gilang", "Gunawan", "Hadi", "Hari", "Hendra",
    "Indra", "Iwan", "Jaka", "Joko", "Kiki", "Lilik", "Lutfi", "Mahdi", "Mahendra", "Maman",
    "Mardi", "Miftah", "Nana", "Nur", "Oki", "Paiman", "Pandu", "Purnomo", "Rahman", "Rizky",
    "Rusdi", "Samsul", "Sigit", "Sukma", "Surya", "Taufik", "Toni", "Tri", "Usman", "Wahyu",
    "Wawan", "Widodo", "Yanto", "Yoga", "Yusuf", "Zaki", "Zain", "Zulfi", "Aldo", "Alex",
    "Alvin", "Andi", "Argo", "Bambang", "Bobby", "Bonar", "Budi", "Dede", "Dian", "Dio",
    "Dony", "Eko", "Elang", "Fahmi", "Fauzi", "Fikri", "Galang", "Gilang", "Hadi", "Hanafi",
    "Hari", "Hendra", "Heri", "Husni", "Iksan", "Imam", "Indra", "Irwan", "Jaka", "Joko",
    "Kamal", "Kiki", "Lukman", "Mahdi", "Mahendra", "Maman", "Mardi", "Miftah", "Nana", "Nur",
    "Oki", "Paiman", "Pandu", "Purnomo", "Rahman", "Rizky", "Rusdi", "Samsul", "Sigit", "Sukma",
    "Surya", "Taufik", "Toni", "Tri", "Usman", "Wahyu", "Wawan", "Widodo", "Yanto", "Yoga",
    "Yusuf", "Zaki", "Zain", "Zulfi", "Aldo", "Alex", "Alvin", "Andi", "Argo", "Bambang",
    "Bobby", "Bonar", "Budi", "Dede", "Dian", "Dio", "Dony", "Eko", "Elang", "Fahmi",
    "Fauzi", "Fikri", "Galang", "Gilang", "Hadi", "Hanafi", "Hari", "Hendra", "Heri", "Husni",
    "Iksan", "Imam", "Indra", "Irwan", "Jaka", "Joko", "Kamal", "Kiki", "Lukman", "Mahdi",
    "Mahendra", "Maman", "Mardi", "Miftah", "Nana", "Nur", "Oki", "Paiman", "Pandu", "Purnomo",
    "Rahman", "Rizky", "Rusdi", "Samsul", "Sigit", "Sukma", "Surya", "Taufik", "Toni", "Tri",
    "Usman", "Wahyu", "Wawan", "Widodo", "Yanto", "Yoga", "Yusuf", "Zaki", "Zain", "Zulfi",
    "Aldo", "Alex", "Alvin", "Andi", "Argo", "Bambang", "Bobby", "Bonar", "Budi", "Dede",
    "Dian", "Dio", "Dony", "Eko", "Elang", "Fahmi", "Fauzi", "Fikri", "Galang", "Gilang",
    "Hadi", "Hanafi", "Hari", "Hendra", "Heri", "Husni", "Iksan", "Imam", "Indra", "Irwan",
    "Jaka", "Joko", "Kamal", "Kiki", "Lukman", "Mahdi", "Mahendra", "Maman", "Mardi", "Miftah",
    "Nana", "Nur", "Oki", "Paiman", "Pandu", "Purnomo", "Rahman", "Rizky", "Rusdi", "Samsul",
    "Sigit", "Sukma", "Surya", "Taufik", "Toni", "Tri", "Usman", "Wahyu", "Wawan", "Widodo",
    "Yanto", "Yoga", "Yusuf", "Zaki", "Zain", "Zulfi", "Aldo", "Alex", "Alvin", "Andi",
    "Argo", "Bambang", "Bobby", "Bonar", "Budi", "Dede", "Dian", "Dio", "Dony", "Eko",
    "Elang", "Fahmi", "Fauzi", "Fikri", "Galang", "Gilang", "Hadi", "Hanafi", "Hari", "Hendra",
    "Heri", "Husni", "Iksan", "Imam", "Indra", "Irwan", "Jaka", "Joko", "Kamal", "Kiki",
    "Lukman", "Mahdi", "Mahendra", "Maman", "Mardi", "Miftah", "Nana", "Nur", "Oki", "Paiman",
    "Pandu", "Purnomo", "Rahman", "Rizky", "Rusdi", "Samsul", "Sigit", "Sukma", "Surya", "Taufik",
    "Toni", "Tri", "Usman", "Wahyu", "Wawan", "Widodo", "Yanto", "Yoga", "Yusuf", "Zaki",
    "Zain", "Zulfi", "Aldo", "Alex", "Alvin", "Andi", "Argo", "Bambang", "Bobby", "Bonar",
    "Budi", "Dede", "Dian", "Dio", "Dony", "Eko", "Elang", "Fahmi", "Fauzi", "Fikri",
    "Galang", "Gilang", "Hadi", "Hanafi", "Hari", "Hendra", "Heri", "Husni", "Iksan", "Imam",
    "Indra", "Irwan", "Jaka", "Joko", "Kamal", "Kiki", "Lukman", "Mahdi", "Mahendra", "Maman",
    "Mardi", "Miftah", "Nana", "Nur", "Oki", "Paiman", "Pandu", "Purnomo", "Rahman", "Rizky",
    "Rusdi", "Samsul", "Sigit", "Sukma", "Surya", "Taufik", "Toni", "Tri", "Usman", "Wahyu",
    "Wawan", "Widodo", "Yanto", "Yoga", "Yusuf", "Zaki", "Zain", "Zulfi"
]
# Fungsi untuk menghasilkan nama acak
def generate_random_name():
    return random.choice(nama_depan)

# Jumlah nama yang ingin dihasilkan
jumlah_nama = 50

# Hasilkan nama acak dan simpan dalam daftar
nama_list = []
for _ in range(jumlah_nama):
    nama_acak = generate_random_name()
    nama_list.append(f"sv {nama_acak},lagi butkon")
    nama_list.append(f"sv bang {nama_acak}lagi butkon (butuh kontak)")
    nama_list.append(f"sv kak {nama_acak},nambah kontak")
    nama_list.append(f"sv gw {nama_acak},push kontak")
    nama_list.append(f"sv cuy nama gw {nama_acak}lagi push kontak")
    nama_list.append(f"sv kak,bg nama gw  {nama_acak},sv ya lagi butkon")
    nama_list.append(f"sebut nama langsung gw sv nama gw {nama_acak}")
    nama_list.append(f"sv lagi butuh kontak nama gw {nama_acak}")
    nama_list.append(f"sv {nama_acak} dari grup,lagi butkon")
    nama_list.append(f"sv  {nama_acak} dari grup tapi gw dh out")
    nama_list.append(f"sv {nama_acak} lagi butuh kontak aj")
    nama_list.append(f"sv {nama_acak} numpan nonton sw doang wkwkwk")











# Acak urutan nama dalam daftar
random.shuffle(nama_list)

# Simpan hasil ke file p.txt
with open("p.txt", "w") as file:
    for nama in nama_list:
        file.write(f"{nama}\n")

print(f"{jumlah_nama} nama acak telah dihasilkan dan disimpan di p.txt")
