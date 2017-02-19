#!/usr/bin/env python
import os
import click
from flask.cli import FlaskGroup
from application import create_app


@click.group(cls=FlaskGroup, create_app=lambda info: create_app())
def cli():
    pass


@cli.group(name="db", short_help="Manage database")
def database():
    pass


@cli.command(short_help="Run unittest")
def test():
    os.system('python -m unittest')


@database.command(short_help="Init db")
def init():
    from application.model import db
    print("Init db!")
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    cli()
