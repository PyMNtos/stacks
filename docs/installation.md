Installation for Stacks
=======================

This document assumes *nix type environment.

Setup Basic Development Tools
-----------------------------

Follow the instructions for your OS on this wiki page:

    https://github.com/PyMNtos/stacks/wiki/Dev-Environment-Setup

Install Dependencies
--------------------

Install Postgres:

    sudo apt-get install postgresql libpq-dev

Configuring Postgres
--------------------

Log into Postgres and setup the password for the default `postgres` user:

    sudo -u postgres psql postgres

At the PSQL prompt, enter the following command and set the password to `postgres`:

    \password postgres

Now create a database and verde user in Postgres:

    CREATE DATABASE stacks;
    CREATE USER stacks WITH PASSWORD 'stacks';
    GRANT ALL PRIVILEGES ON DATABASE stacks TO stacks;
    \q # To quit

Create Virtual Environment
--------------------------

Create a virtual environment named `stacks`.

    mkvirtualenv stacks

Switch into virtual environment using VirtualEnvWrapper tools:

    workon stacks

Install requirements.txt
------------------------

Change directory into the Stacks root directory and run:

    pip install -r requirements.txt

Setup the database
------------------

Run this on a fresh install to sync the db:

    python manage.py syncdb

Use the following for `syncdb`:

Username: `stacks`

Email: `stacks@github.com`

Password: `stacks`

Performing Initial Migrations and Fixtures
-------------------------------------------

Then migrate with South:

    python manage.py migrate

