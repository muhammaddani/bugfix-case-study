# Contributing

Terima kasih atas minatmu! Repo ini adalah proyek portofolio kecil, tetapi
kontribusi tetap diterima.

## Menjalankan proyek secara lokal

```bash
git clone https://github.com/muhammaddani/bugfix-case-study.git
cd bugfix-case-study
pip install -r requirements.txt
pytest -v
```

## Alur kontribusi

1. Buat branch baru: `git checkout -b fix/nama-perbaikan`
2. Lakukan perubahan dan **tambahkan test** yang membuktikannya.
3. Pastikan semua test lulus: `pytest -v`
4. Commit dengan pesan yang jelas (lihat gaya di bawah).
5. Buka Pull Request.

## Gaya commit

- `feat: ...` — fitur baru
- `fix: ...` — perbaikan bug
- `docs: ...` — perubahan dokumentasi
- `test: ...` — menambah atau memperbaiki test
- `chore: ...` — pekerjaan rumah tangga

## Konvensi bug

Setiap bug yang dicatat sebaiknya punya entri di `BUGS.md` dengan tiga bagian:
**gejala**, **akar masalah**, dan **perbaikan** — beserta test yang membuktikannya.