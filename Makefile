.PHONY: build
build:
	@echo "Building..."
	python setup.py sdist bdist_wheel --universal
	@echo "Building... Done"

.PHONY: clean
clean:
	@echo "Cleaning..."
	rm -rf build dist scapy_helper.egg-info
	@echo "Cleaning... Done"

.PHONY: format
format:
	@echo "Formatting..."
	python -m black -t py36 .
	python -m isort packet_helper/ scapy_helper/ test/ --profile black
	@echo "Formatting... Done"

.PHONY: publish
publish: clean format build
	twine upload dist/*

.PHONY: test
test:
	python -m pytest

.PHONY: test-mypy
test-mypy:
	python -m mypy scapy_helper/ test/

.PHONY: version
version:
	python tools/version_checker.py
