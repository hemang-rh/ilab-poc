#!/bin/sh
set -e

if [ $# -eq 0 ]; then
    echo "Please provide a command. Available commands:"
    echo "  convertdoc FILEPATH"
    echo "  convertdocs --INPUTDIR --OUTPUTDIR"
    echo ""
    echo "Global options:"
    echo "  --log-level [DEBUG|INFO|WARNING|ERROR]"
    exit 1
fi

exec ilabcli "$@"