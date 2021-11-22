run:
	@echo "Running Application..."
	docker-compose up -d --build

.PHONY: test
test:
	@echo "Running tests..."
	pipenv run pytest -vv

DEFAULT_COMMIT_COMMENT="updating code"
deploy:
	@echo "Deploying application"
	cp .env ansible/.env
	pipenv run ansible-playbook ansible/deploy.yml -i ansible/hosts -K
