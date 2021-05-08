#!/bin/bash
set -x

sudo docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
psql postgresql://postgres:docker@localhost:5432 -c 'DROP DATABASE backtester'

set -e
psql postgresql://postgres:docker@localhost:5432 -c 'CREATE DATABASE backtester'
psql postgresql://postgres:docker@localhost:5432/backtester -a -f schema.sql
../venv/bin/python3 upload_quotes.py
sudo mv quotes $HOME/docker/volumes/postgres
psql postgresql://postgres:docker@localhost:5432/backtester -a -f copy_quotes.sql
psql postgresql://postgres:docker@localhost:5432/backtester -a -f init.sql
