.PHONY: .FORCE

build: .FORCE
	python setup.py sdist bdist_wheel

upload: .FORCE
	python -m twine upload --verbose  --repository-url https://test.pypi.org/legacy/ dist/*

install-dev: .FORCE
	python -m pip install -e .

uninstall: .FORCE
	python -m pip uninstall luri

clean:
	rm -rf luri.egg-info
	rm -rf dist
	rm -rf build

version:
	#run tests
	#update changelog.md
	#change version num in setup.py
	#git commit -F changelog.md
	#git push origin master
	#build bdist_wheel
	#upload to pypi
	
