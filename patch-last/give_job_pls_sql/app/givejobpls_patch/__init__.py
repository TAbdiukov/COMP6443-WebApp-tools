#!/usr/bin/env python3

# This is the entrypoint to givejobpls_patch

from flask_core.app import create_app
from flask_core.config import Config

from . import models  # noqa

# If you add more blueprints, add them here
from .main import bp as main_bp

config = Config()
app = create_app(config)

app.register_blueprint(main_bp)
