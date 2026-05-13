activate:
	powershell -NoExit -ExecutionPolicy Bypass -Command ". .\.venv\Scripts\Activate.ps1"

migrate:
	python manage.py migrate

start:
	python manage.py runserver 0.0.0.0:8000

tailwind:
	npx @tailwindcss/cli -i static/css/style.css -o static/css/tailwind.css --minify --watch

.PHONY: activate migrate start tailwind