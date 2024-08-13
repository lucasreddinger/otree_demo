#!/bin/bash

# To use this file, execute `source path/to/otree_gpr.sh`

# This should be the path to a valid virtual python environment
source /home/`whoami`/.venv/otree_demo/bin/activate

export OTREE_AUTH_LEVEL="DEMO"
export OTREE_ADMIN_PASSWORD="somepassword"

# Set this appropriately for production usage
export DATABASE_URL=postgres://username:password@localhost/database

# Comment this line for development
export OTREE_PRODUCTION=1

