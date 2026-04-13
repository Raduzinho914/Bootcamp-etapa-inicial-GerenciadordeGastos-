import django
from django.conf import settings

def pytest_configure(config):
    # Trava de segurança: só configura se já não estiver configurado pelo VS Code/Plugin
    if not settings.configured:
        settings.configure(
            DATABASES={
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": ":memory:",
                }
            },
            INSTALLED_APPS=[
                'django.contrib.contenttypes',
                'django.contrib.auth',
                
                "gastos"
            ],
            DEFAULT_AUTO_FIELD='django.db.models.AutoField',
        )
        django.setup()