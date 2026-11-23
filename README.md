# Bugfix Case Study

[![CI](https://github.com/muhammaddani/bugfix-case-study/actions/workflows/ci.yml/badge.svg)](https://github.com/muhammaddani/bugfix-case-study/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

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
├── inventory_buggy.py      # versi awal yang sengaja buggy
├── tests/
│   ├── test_inventory.py           # 15 test (lulus)
│   └── test_buggy_demonstration.py # 4 test bug (xfail)
├── .github/workflows/
│   └── ci.yml              # CI: jalankan test di setiap push
├── BUGS.md                 # catatan tiap bug: gejala, akar masalah, perbaikan
├── pytest.ini
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