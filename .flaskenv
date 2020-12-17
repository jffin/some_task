# FLASK_ENV=production
FLASK_ENV=development
FLASK_APP=text_api.app:create_app
SECRET_KEY=7b402d65-0785-4494-a766-4aaeca8521ff
DATABASE_URI=sqlite:////db/text_api.db

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND_URL=redis://redis:6379/0
CELERY_DATABASE_URI=sqlite:////code/db/text_api.db
