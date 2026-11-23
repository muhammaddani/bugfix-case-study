"""Versi AWAL modul inventory -- SENGAJA MENGANDUNG BUG.

File ini disimpan sebagai bukti kondisi "sebelum perbaikan".
Lihat inventory.py untuk versi yang sudah diperbaiki.
Jalankan test terhadap file ini untuk melihat kegagalannya.
"""

from __future__ import annotations


class Inventory:
    def __init__(self) -> None:
        self._items: dict[str, dict] = {}

    def add_item(self, code: str, name: str, price: float, quantity: int) -> None:
        self._items[code] = {
            "name": name,
            "price": price,
            "quantity": quantity,
        }

    def get_item(self, code: str) -> dict | None:
        return self._items.get(code)

    # BUG 1: urutan operasi salah -> total nilai stok tidak akurat
    def total_value(self) -> float:
        return sum(item["price"] for item in self._items.values()) * len(self._items)

    # BUG 2: tidak ada validasi -> stok bisa jadi negatif
    def remove_stock(self, code: str, amount: int) -> None:
        item = self._items.get(code)
        if item is not None:
            item["quantity"] -= amount

    # BUG 3: pencarian kode case-sensitive -> "AB12" != "ab12"
    def find_by_code(self, code: str) -> dict | None:
        return self._items.get(code)

    # BUG 4: menghapus item yang tidak ada gagal tanpa laporan
    def delete_item(self, code: str) -> None:
        self._items.pop(code, None)

    def restock(self, code: str, amount: int) -> None:
        item = self._items.get(code)
        if item is not None:
            item["quantity"] += amount