from lettuce import step, world, before
from nose.tools import assert_equals

from app.application import app
from app.views import USERS


@before.all
def before_all():
    world.app = app.test_client()

@step(u'Given some users are in the system')
def given _some_users_are_in_the_system(step):
    USERS.update({'david01': {'name': 'David Sale'}})
