all: build install

.PHONY: build install test docs distclean dist upload

build:
	python setup.py build

install: build
	python setup.py install

test:
	pytest --cov-report term --cov=bananompy test/

docs:
	cd docs;\
	make html
	# open _build/html/index.html

check:
	python -m twine check dist/*

distclean:
	rm dist/*

dist:
	python setup.py sdist bdist_wheel --universal

register:
	python setup.py register

up:
	python -m twine upload dist/*

uptest:
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*