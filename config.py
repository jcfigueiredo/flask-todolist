# -*- coding: utf-8 -*-

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def create_uri(db_name, use_sqlite=False):
    return os.environ.get('SQLALCHEMY_DATABASE_URI') or f'sqlite:///{os.path.join(BASEDIR, db_name)}.db'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key, just for testing'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = create_uri('todolist-dev')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = create_uri('todolist-test')
    WTF_CSRF_ENABLED = False
    import logging
    logging.basicConfig(
        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
    )
    logging.getLogger().setLevel(logging.DEBUG)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = create_uri('todolist')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
