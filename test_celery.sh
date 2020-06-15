#!/bin/bash
export PCONFIG=Test
python -m celery --app=worker.celery worker -c 8 --loglevel=info
