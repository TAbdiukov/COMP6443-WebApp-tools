#!/usr/bin/env bash

export FLASK_CORE_CONFIG="$(realpath config.py)"

python ./app/entrypoint.py
