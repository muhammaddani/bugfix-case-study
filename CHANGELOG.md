# Changelog

Semua perubahan penting pada proyek ini didokumentasikan di file ini.

Format mengikuti [Keep a Changelog](https://keepachangelog.com/) dan proyek ini
menganut [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-11-23

### Ditambahkan
- Modul `inventory` versi perbaikan dengan validasi lengkap.
- Modul `inventory_buggy` sebagai titik awal yang sengaja mengandung 4 bug.
- 15 test otomatis yang membuktikan perbaikan (pytest).
- 4 test demonstrasi bug yang ditandai `xfail`.
- Dokumentasi lengkap tiap bug di `BUGS.md`.
- CI GitHub Actions pada Python 3.10–3.12.
- `Makefile`, `CONTRIBUTING.md`, dan `pyproject.toml`.

### Diperbaiki
- **BUG 1** — `total_value()` menghitung total nilai stok dengan benar.
- **BUG 2** — stok tidak lagi bisa menjadi negatif.
- **BUG 3** — pencarian kode produk tidak sensitif huruf besar/kecil.
- **BUG 4** — menghapus item yang tidak ada kini melaporkan error.