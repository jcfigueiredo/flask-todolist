# -*- coding: utf-8 -*-

import os
import logging, logging.config
import yaml

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def create_uri(db_name):
    return os.environ.get('SQLALCHEMY_DATABASE_URI') or f'sqlite:///{os.path.join(BASEDIR, db_name)}.db'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key, just for testing'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        logging_conf_path = os.path.join(os.path.abspath(os.path.curdir), 'logging.yml')

        with open(logging_conf_path, 'r') as stream:
            try:
                logging.config.dictConfig(yaml.load(stream))
            except yaml.YAMLError as exc:
                print(exc)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = create_uri('todolist-dev')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = create_uri('todolist-test')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = create_uri('todolist')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
