run:
	@echo "Running Application..."
	docker-compose up -d --build

test:
	@echo "Running tests..."
	pipenv run pytest -vv

DEFAULT_COMMIT_COMMENT="updating code"
deploy:
	echo "Deploying application"
	git add .
	git commit -am $(DEFAULT_COMMIT_COMMENT)
	pipenv run ansible-playbook ansible/deploy.yml ansible/hosts -K
