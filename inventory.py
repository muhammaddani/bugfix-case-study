"""Modul inventory -- versi yang sudah diperbaiki.

Setiap perbaikan terhadap inventory_buggy.py ditandai dengan komentar
"BUG n" agar mudah ditelusuri. Penjelasan lengkap ada di BUGS.md.
"""

from __future__ import annotations


class InventoryError(Exception):
    """Error dasar untuk operasi inventory yang tidak valid."""


class ItemNotFoundError(InventoryError):
    """Dilempar saat kode produk tidak ditemukan."""


class InsufficientStockError(InventoryError):
    """Dilempar saat pengurangan stok melebihi jumlah yang tersedia."""


class Inventory:
    """Inventori sederhana yang menyimpan item berdasarkan kode produk.

    Kode produk dinormalisasi (spasi dipangkas, huruf jadi kapital) sehingga
    pencarian tidak sensitif terhadap huruf besar/kecil.
    """

    def __init__(self) -> None:
        self._items: dict[str, dict] = {}

    # -- helper -----------------------------------------------------------

    @staticmethod
    def _normalize(code: str) -> str:
        if not isinstance(code, str):
            raise InventoryError(f"Kode produk harus teks, bukan {type(code).__name__}.")
        return code.strip().upper()

    # -- operasi utama ----------------------------------------------------

    def add_item(self, code: str, name: str, price: float, quantity: int) -> None:
        if price < 0:
            raise InventoryError("Harga tidak boleh negatif.")
        if quantity < 0:
            raise InventoryError("Jumlah awal tidak boleh negatif.")
        self._items[self._normalize(code)] = {
            "name": name,
            "price": float(price),
            "quantity": int(quantity),
        }

    def get_item(self, code: str) -> dict | None:
        """Ambil salinan data item, atau None jika tidak ada."""
        item = self._items.get(self._normalize(code))
        return dict(item) if item is not None else None

    def find_by_code(self, code: str) -> dict | None:
        """Cari item tanpa peduli huruf besar/kecil (BUG 3)."""
        return self.get_item(code)

    def total_value(self) -> float:
        """Total nilai stok = jumlah (harga * kuantitas) tiap item (BUG 1)."""
        return sum(item["price"] * item["quantity"] for item in self._items.values())

    def remove_stock(self, code: str, amount: int) -> None:
        """Kurangi stok, tolak jika hasilnya akan negatif (BUG 2)."""
        item = self._require(code)
        if amount < 0:
            raise InventoryError("Jumlah pengurangan tidak boleh negatif.")
        if amount > item["quantity"]:
            raise InsufficientStockError(
                f"Stok {code} hanya {item['quantity']}, tidak cukup untuk mengurangi {amount}."
            )
        item["quantity"] -= amount

    def restock(self, code: str, amount: int) -> None:
        if amount < 0:
            raise InventoryError("Jumlah penambahan tidak boleh negatif.")
        item = self._require(code)
        item["quantity"] += amount

    def delete_item(self, code: str) -> None:
        """Hapus item; laporkan jika kode tidak ditemukan (BUG 4)."""
        normalized = self._normalize(code)
        if normalized not in self._items:
            raise ItemNotFoundError(f"Produk dengan kode {code} tidak ditemukan.")
        del self._items[normalized]

    # -- internal ---------------------------------------------------------

    def _require(self, code: str) -> dict:
        normalized = self._normalize(code)
        item = self._items.get(normalized)
        if item is None:
            raise ItemNotFoundError(f"Produk dengan kode {code} tidak ditemukan.")
        return item