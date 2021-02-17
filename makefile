all: clean build publish

clean:
	@echo "Cleaning..."
	rm -rf build dist scapy_helper.egg-info
	@echo "Cleaning... Done"

build:
	@echo "Building..."
	python setup.py sdist bdist_wheel --universal
	@echo "Building... Done"

publish:
	twine upload dist/*
