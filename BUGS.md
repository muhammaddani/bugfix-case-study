# Catatan Bug

Dokumen ini merinci setiap bug pada `inventory_buggy.py`, cara menemukannya,
akar masalahnya, dan perbaikannya di `inventory.py`.

---

## BUG 1 — Total nilai stok salah

**Gejala**
`total_value()` menghasilkan angka yang tidak sesuai: harga dijumlahkan lalu
dikalikan jumlah item, bukan menjumlahkan harga × kuantitas tiap item.

**Kode bermasalah**
```python
return sum(item["price"] for item in self._items.values()) * len(self._items)
```

**Akar masalah**
Urutan operasi keliru. Untuk 2 item (45000,10) dan (25000,5), rumus salah
menghasilkan `(45000 + 25000) * 2 = 140000`, sedangkan nilai sebenarnya
`45000*10 + 25000*5 = 575000`.

**Perbaikan**
```python
return sum(item["price"] * item["quantity"] for item in self._items.values())
```

**Test yang membuktikan**
`tests/test_inventory.py::TestBug1TotalValue`

---

## BUG 2 — Stok bisa menjadi negatif

**Gejala**
`remove_stock()` mengurangi stok tanpa batas, sehingga kuantitas bisa negatif.

**Kode bermasalah**
```python
item["quantity"] -= amount   # tanpa pemeriksaan
```

**Akar masalah**
Tidak ada validasi terhadap jumlah yang tersedia maupun nilai negatif.

**Perbaikan**
- Tolak jumlah pengurangan negatif.
- Lempar `InsufficientStockError` jika melebihi stok.
- Pastikan stok tidak berubah saat operasi gagal.

**Test yang membuktikan**
`tests/test_inventory.py::TestBug2NonNegativeStock`

---

## BUG 3 — Pencarian kode sensitif huruf besar/kecil

**Gejala**
`find_by_code("ab12")` tidak menemukan item yang tersimpan sebagai `"AB12"`.

**Akar masalah**
Kode disimpan dan dicari apa adanya, tanpa normalisasi.

**Perbaikan**
Normalisasi kode (pangkas spasi, ubah ke huruf kapital) di satu helper
`_normalize()`, dipakai konsisten oleh semua operasi.

**Test yang membuktikan**
`tests/test_inventory.py::TestBug3CaseInsensitiveLookup`

---

## BUG 4 — Menghapus item tak ada gagal secara diam

**Gejala**
`delete_item("ZZZZ")` untuk kode yang tidak ada tidak memberi laporan apa pun,
sehingga pemanggil mengira penghapusan berhasil.

**Kode bermasalah**
```python
self._items.pop(code, None)   # diam-diam mengabaikan ketiadaan
```

**Akar masalah**
Kegagalan disembunyikan, menyulitkan pelacakan masalah.

**Perbaikan**
Lempar `ItemNotFoundError` jika kode tidak ditemukan.

**Test yang membuktikan**
`tests/test_inventory.py::TestBug4DeleteReportsMissing`

---

## Perbaikan tambahan (bukan bug, tapi memperbaiki desain)

- `get_item()` kini mengembalikan **salinan**, sehingga data internal tidak
  bisa diubah dari luar secara tak sengaja.
- Ditambahkan validasi pada `add_item()` (harga dan jumlah tidak boleh negatif).
- Hierarki error yang jelas: `InventoryError` sebagai dasar, dengan
  `ItemNotFoundError` dan `InsufficientStockError` sebagai turunannya.

## Cara mereproduksi

```bash
# Test terhadap kode perbaikan: harus lulus semua
pytest -v

# Test yang mendemonstrasikan bug pada kode awal: ditandai xfail
pytest tests/test_buggy_demonstration.py -v
```