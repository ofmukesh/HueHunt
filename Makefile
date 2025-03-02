# Makefile for Django project

# Variables
PYTHON=python3
PIP=pip
MANAGE=src/manage.py
APPS=account game_profile live_game user_game payment _setting

# Targets
.PHONY: help install run migrate createadmin test celery_start celery_stop

help:
	@echo "Makefile for Django project"
	@echo "Usage:"
	@echo "  make install          Install dependencies"
	@echo "  make run              Run the Django development server"
	@echo "  make migrate          Apply database migrations"
	@echo "  make createadmin  Create a superuser"
	@echo "  make test             Run tests"

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(MANAGE) runserver

migrate:
	$(PYTHON) $(MANAGE) makemigrations $(APPS) && $(PYTHON) $(MANAGE) migrate

createadmin:
	$(PYTHON) $(MANAGE) createsuperuser

test:
	$(PYTHON) $(MANAGE) test

cronadd:
	$(PYTHON) $(MANAGE) crontab add

cronls:
	$(PYTHON) $(MANAGE) crontab show

cronrm:
	$(PYTHON) $(MANAGE) crontab remove