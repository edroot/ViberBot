# -*- coding: utf-8 -*-

import os.path

from migrate.versioning import api
from ViberBot.ViberBot.database import db
from ViberBot.config.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
