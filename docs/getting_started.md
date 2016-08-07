# Getting Started
## Software Prerequisites
- Python (tested on 3.5)
- Postgres (tested on 9.5)

## Installation
- Create a Python Virtualenv ([virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) suggested).
- Create a Postgres database with the Hstore extension (`CREATE EXTENSION hstore;`) on the database.
- Set the pertinent environment variables. Currently required:
 - Set `DJANGO_SETTING_MODULE` to `simple_mon_server.settings.dev_settings` note that this is for development only.
 - Set `SECRET_KEY` to something, this isn't important in development.
- Set the database options up one of two ways:
  - Set the environment variables `DB_NAME`, `DB_USER` ,`DB_PW`, `DB_HOST`,  `DB_PORT`
  - Change the settings in `db_settings.py` directly, but please don't commit this back.
- Set the database up by running `manage.py makemigrations` and `manage.py migrate` to apply them. In future, migrations will be comitted here, but the models are in flux at this point.
- There isn't much else right now.
