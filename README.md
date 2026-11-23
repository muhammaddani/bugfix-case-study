# Bugfix Case Study

Studi kasus perbaikan bug pada sebuah modul Python kecil bernama `inventory`.

Repo ini menunjukkan **proses debugging yang nyata**: kode awal sengaja
mengandung bug, disertai test yang gagal. Setiap bug dianalisis, diperbaiki,
lalu dibuktikan lulus test.

## Catatan jujur

Ini adalah **studi kasus latihan**, bukan pekerjaan klien. Tujuannya untuk
menunjukkan kemampuan membaca kode, menemukan akar masalah, dan memperbaikinya
tanpa merusak perilaku yang sudah benar.

## Isi repo

```
bugfix-case-study/
├── inventory.py            # modul yang diperbaiki (versi akhir)
├── tests/
│   └── test_inventory.py   # test otomatis
├── BUGS.md                 # catatan tiap bug: gejala, akar masalah, perbaikan
├── requirements.txt
├── LICENSE
└── README.md
```

## Cara menjalankan test

```bash
pip install -r requirements.txt
pytest -v
```

## Ringkasan bug yang diperbaiki

Lihat detail lengkap di [BUGS.md](BUGS.md). Secara singkat:

1. **Total nilai stok salah** — perkalian dilakukan dengan urutan yang salah
   sehingga jumlah tidak akurat.
2. **Stok tidak boleh negatif** — pengurangan stok bisa menghasilkan angka
   negatif tanpa peringatan.
3. **Pencarian kode tidak konsisten** — kode produk dengan huruf besar/kecil
   berbeda dianggap produk terpisah.
4. **Penghapusan item yang tidak ada tidak dilaporkan** — operasi gagal secara
   diam-diam.

## Lisensi

MIT — lihat [LICENSE](LICENSE).