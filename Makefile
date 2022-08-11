

clean:
	rm -rf build dist *egg*

build: clean
	python3 setup.py sdist

release: build
	twine upload --skip-existing dist/*
