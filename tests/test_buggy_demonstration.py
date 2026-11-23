"""Test yang menunjukkan bug pada inventory_buggy.py.

Jalankan dengan:
    pytest tests/test_buggy_demonstration.py -v

Test di sini SENGAJA mengharapkan perilaku yang benar, sehingga menjadi
GAGAL saat dijalankan terhadap kode yang masih buggy. Ini adalah bukti
kondisi "sebelum perbaikan".

File ini mengimpor modul buggy secara langsung, jadi ia tidak akan
mengganggu test utama pada inventory.py yang sudah diperbaiki.
"""

import pytest

import inventory_buggy as buggy

pytestmark = pytest.mark.xfail(
    reason="Dijalankan terhadap kode yang masih buggy; kegagalan adalah bukti bug.",
    strict=True,
)


def test_bug1_total_value_is_wrong():
    inv = buggy.Inventory()
    inv.add_item("AB12", "Kopi Arabika", 45000, 10)
    inv.add_item("CD34", "Teh Hijau", 25000, 5)
    # Benar: 450000 + 125000 = 575000
    assert inv.total_value() == 575000  # gagal: kode buggy menghitung salah


def test_bug2_stock_can_go_negative():
    inv = buggy.Inventory()
    inv.add_item("AB12", "Kopi Arabika", 45000, 10)
    inv.remove_stock("AB12", 999)
    # Benar: tidak boleh negatif
    assert inv.get_item("AB12")["quantity"] >= 0  # gagal: jadi -989


def test_bug3_lookup_is_case_sensitive():
    inv = buggy.Inventory()
    inv.add_item("AB12", "Kopi Arabika", 45000, 10)
    # Benar: "ab12" harus menemukan item
    assert inv.find_by_code("ab12") is not None  # gagal: None


def test_bug4_delete_missing_is_silent():
    inv = buggy.Inventory()
    with pytest.raises(Exception):
        inv.delete_item("ZZZZ")  # gagal: tidak melempar apa pun