#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from fabric.api import *
from fabric.colors import *


@task
def dump():
    local('python ./manage.py dumpdata > main/fixtures/initial_data.json')


@task
def m():
    local('python ./manage.py schemamigration main --auto')
    local('python ./manage.py migrate main')


@task
def mn(appname):
    local('python ./manage.py schemamigration {} --auto'.format(appname))
    local('python ./manage.py migrate {}'.format(appname))


@task
def push(comment=False):
    if comment == False:
        return red('Commit comment is requred!')
    local('pip freeze > requirements.txt')
    dump()
    #local('find . -name "*.py" -exec isort {} \\;')
    local('autopep8 --in-place -r . ')
    local('git add .')
    local('git status', capture=False)
    local('git commit -m "{}"'.format(comment), capture=False)
    local('git push', capture=False)
    local('git push heroku master')
    green('All ok')


@task
def run():
    local(';\n'.join([
        'python ./manage.py syncdb',
        'python ./manage.py migrate',
        'python ./manage.py collectstatic --noinput',
        'python ./manage.py runserver',
    ]))
