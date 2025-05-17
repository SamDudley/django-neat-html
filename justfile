default:
	@just --list

build:
    poetry build

publish:
	poetry publish

run-example:
	poetry run python example/manage.py runserver
