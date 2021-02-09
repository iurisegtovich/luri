PHONY: .FORCE

build: .FORCE
	python setup.py sdist bdist_wheel

upload: .FORCE
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install-dev: .FORCE
	python -m pip install -e .
