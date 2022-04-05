import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generate conf for nats-api"

    def handle(self, *args, **kwargs):

        self.stdout.write("Creating configuration for nats-api...")
        db = settings.DATABASES["default"]
        if hasattr(settings, "DB_SSL") or "DB_SSL" in os.environ:
            ssl = settings.DB_SSL
        else:
            ssl = "disable"

        config = {
            "key": settings.SECRET_KEY,
            "natsurl": f"tls://{settings.ALLOWED_HOSTS[0]}:4222",
            "user": db["USER"],
            "pass": db["PASSWORD"],
            "host": db["HOST"],
            "port": int(db["PORT"]),
            "dbname": db["NAME"],
            "sslmode": ssl,
        }
        conf = os.path.join(settings.BASE_DIR, "nats-api.conf")
        with open(conf, "w") as f:
            json.dump(config, f)

        self.stdout.write("Configuration for nats-api created successfully")
