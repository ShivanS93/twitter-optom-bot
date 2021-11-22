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
	git add .
	git commit -am $(DEFAULT_COMMIT_COMMENT)
	cp .env ansible/.env
	pipenv run ansible-playbook ansible/deploy.yml -i ansible/hosts -K
