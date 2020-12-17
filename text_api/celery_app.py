from text_api.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ('text_api.tasks.sentences',)
