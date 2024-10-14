default:
	@just --list

build:
    poetry build

publish:
	poetry publish
