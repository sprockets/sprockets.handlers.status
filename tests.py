"""
Tests for the sprockets.handlers.status package

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import uuid

import mock

from sprockets.handlers import status


class MockApplication(object):
    ui_methods = {}
    ui_modules = {}



class TestSetApplication(unittest.TestCase):

    def test_set_application_sets_application(self):
        application = str(uuid.uuid4)
        status.set_application(application)
        self.assertEqual(status.APPLICATION, application)


class TestStatusHandlerPackageVersion(unittest.TestCase):

    def test_valid_application_version_isnt_unknown(self):
        status.set_application('nose')
        self.assertNotEqual(status.StatusHandler._package_version(),
                            status.UNKNOWN)

    def test_valid_application_version_is_unknown(self):
        status.set_application(str(uuid.uuid4()))
        self.assertEqual(status.StatusHandler._package_version(),
                         status.UNKNOWN)


class TestCase(unittest.TestCase):

    @mock.patch('tornado.httputil.HTTPServerRequest')
    def setUp(self, request):
        self.application = MockApplication()
        self.request = request
        self.obj = status.StatusHandler(self.application, self.request)


class TestStatusHandlerStatusAttribute(TestCase):

    def test_when_status_is_not_set(self):
        self.assertEqual(self.obj._application_status(), status.OK)

    def test_when_status_is_set_to_maintenance(self):
        setattr(self.application, 'status', status.MAINTENANCE)
        self.assertEqual(self.obj._application_status(), status.MAINTENANCE)


class TestStatusHandlerResponseCodes(TestCase):

    def test_when_status_is_not_set(self):
        self.assertEqual(self.obj._status_response_code(), 200)

    def test_when_status_is_set_to_maintenance(self):
        setattr(self.application, 'status', status.MAINTENANCE)
        self.assertEqual(self.obj._status_response_code(), 503)

    def test_when_status_is_set_to_error(self):
        setattr(self.application, 'status','error')
        self.assertEqual(self.obj._status_response_code(), 500)
