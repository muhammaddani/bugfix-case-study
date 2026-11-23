"""Test untuk modul inventory (versi perbaikan).

Setiap kelompok test memetakan ke satu bug yang dijelaskan di BUGS.md.
"""

import pytest

from inventory import (
    Inventory,
    InsufficientStockError,
    InventoryError,
    ItemNotFoundError,
)


def make_inventory() -> Inventory:
    inv = Inventory()
    inv.add_item("AB12", "Kopi Arabika", 45000, 10)
    inv.add_item("CD34", "Teh Hijau", 25000, 5)
    return inv


class TestBug1TotalValue:
    """BUG 1: total nilai stok harus jumlah (harga * kuantitas)."""

    def test_total_value_is_price_times_quantity(self):
        inv = make_inventory()
        # 45000*10 + 25000*5 = 450000 + 125000 = 575000
        assert inv.total_value() == 575000

    def test_total_value_empty_is_zero(self):
        assert Inventory().total_value() == 0

    def test_total_value_not_double_counted(self):
        inv = make_inventory()
        value = inv.total_value()
        inv.total_value()
        assert inv.total_value() == value


class TestBug2NonNegativeStock:
    """BUG 2: stok tidak boleh menjadi negatif."""

    def test_remove_stock_within_bounds(self):
        inv = make_inventory()
        inv.remove_stock("AB12", 4)
        assert inv.get_item("AB12")["quantity"] == 6

    def test_remove_too_much_raises(self):
        inv = make_inventory()
        with pytest.raises(InsufficientStockError):
            inv.remove_stock("AB12", 999)

    def test_stock_never_negative_after_failed_removal(self):
        inv = make_inventory()
        with pytest.raises(InsufficientStockError):
            inv.remove_stock("AB12", 999)
        assert inv.get_item("AB12")["quantity"] == 10

    def test_negative_amount_rejected(self):
        inv = make_inventory()
        with pytest.raises(InventoryError):
            inv.remove_stock("AB12", -5)


class TestBug3CaseInsensitiveLookup:
    """BUG 3: pencarian kode tidak boleh sensitif huruf besar/kecil."""

    def test_lowercase_finds_item(self):
        inv = make_inventory()
        assert inv.find_by_code("ab12") is not None

    def test_mixed_case_finds_item(self):
        inv = make_inventory()
        assert inv.find_by_code("Ab12")["name"] == "Kopi Arabika"

    def test_whitespace_is_trimmed(self):
        inv = make_inventory()
        assert inv.find_by_code("  cd34  ")["name"] == "Teh Hijau"


class TestBug4DeleteReportsMissing:
    """BUG 4: menghapus item yang tidak ada harus dilaporkan, bukan diam."""

    def test_delete_existing(self):
        inv = make_inventory()
        inv.delete_item("ab12")
        assert inv.get_item("AB12") is None

    def test_delete_missing_raises(self):
        inv = make_inventory()
        with pytest.raises(ItemNotFoundError):
            inv.delete_item("ZZZZ")

    def test_delete_missing_does_not_remove_others(self):
        inv = make_inventory()
        with pytest.raises(ItemNotFoundError):
            inv.delete_item("ZZZZ")
        assert inv.get_item("CD34") is not None


class TestGetItemReturnsCopy:
    """get_item mengembalikan salinan, agar data internal tidak bisa diubah liar."""

    def test_mutation_of_returned_item_does_not_affect_store(self):
        inv = make_inventory()
        item = inv.get_item("AB12")
        item["quantity"] = 0
        assert inv.get_item("AB12")["quantity"] == 10

    def test_get_missing_returns_none(self):
        assert make_inventory().get_item("NOPE") is None