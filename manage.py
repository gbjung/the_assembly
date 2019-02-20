#!/usr/bin/env python
import os
import sys
import environ

if __name__ == "__main__":
    env = environ.Env(DEBUG=(bool, False),)
    environ.Env.read_env()

    if env('ENV_SETTING') == 'dev':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "theassembly.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "theassembly.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
