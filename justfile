# justfile -- alternatif ringkas jika kamu memakai `just`
# (https://github.com/casey/just). Pengguna Windows tanpa `just` bisa
# memakai `python tasks.py <tugas>`.

default:
    @just --list

install:
    python -m pip install --upgrade pip
    pip install -r requirements.txt

test:
    pytest -v

test-buggy:
    pytest tests/test_buggy_demonstration.py -v

clean:
    python tasks.py clean