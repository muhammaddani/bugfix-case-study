.PHONY: help install test clean

help:  ## Tampilkan daftar perintah
	@echo "Perintah yang tersedia:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-12s %s\n", $$1, $$2}'

install:  ## Pasang dependensi (termasuk pytest)
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:  ## Jalankan seluruh test
	pytest -v

test-buggy:  ## Tunjukkan bug pada kode awal (xfail)
	pytest tests/test_buggy_demonstration.py -v

clean:  ## Hapus artefak cache
	rm -rf .pytest_cache __pycache__ tests/__pycache__ .coverage htmlcov
	find . -name "*.pyc" -delete