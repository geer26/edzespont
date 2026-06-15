#!/bin/bash

set -euo pipefail

############################################################
# Help                                                     #
############################################################
Help()
{
    echo "Autogenerate and run migrations"
    echo "!!!DO NOT FORGET TO VERIFY THE GENERATED MIGRATION SCRIPT!!!"
    echo "options:"
    echo "apply|-a     Apply migration"
    echo "generate|-g <migration label>     Generate migration"
    echo "help|-h     Print this Help."
    exit 1
}
############################################################
# Generation                                               #
############################################################
Generate()
{
    local migration_name="$1"
    alembic revision --autogenerate -m "$migration_name"
    echo "Migration script generated!"
    exit 1
}

############################################################
# Generation                                               #
############################################################
Apply()
{
    alembic upgrade head
    echo "Migration done!"
    exit 1
}

############################################################
# Main
############################################################
case "$1" in
    apply|-a)
        Apply
        ;;
    generate|-g)
        Generate "$2"
        ;;
    help|-h|"")
        Help
        ;;
    *)
        echo "Unknown option: $1"
        echo
        Help
        exit 1
        ;;
esac
