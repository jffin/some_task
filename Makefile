.PHONY: init init-migration build run db-migrate test tox

init:  build run
	docker-compose exec web text_api db upgrade
	docker-compose exec web text_api init
	@echo "Init done, containers running"

prod-init:  prod-build prod-run
	docker-compose -f production.yml exec flask_web text_api db upgrade
	docker-compose -f production.yml exec flask_web text_api init
	@echo "Init done, containers running, now you can navigate to http://127.0.0.1:8080 in your browser"

build:
	docker-compose build

prod-build:
	docker-compose -f production.yml build

run:
	docker-compose up -d

prod-run:
	docker-compose -f production.yml up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

db-migrate:
	docker-compose exec web text_api db migrate

db-upgrade:
	docker-compose exec web text_api db upgrade

test:
	docker-compose run -v $(PWD)/tests:/code/tests:ro web tox -e test

tox:
	docker-compose run -v $(PWD)/tests:/code/tests:ro web tox -e py38

lint:
	docker-compose run web tox -e lint
