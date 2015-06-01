"""
Tests for the sprockets.handlers.status package

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import uuid

from sprockets.handlers import status

class MockApplication(object):
    pass


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


class TestStatusHandlerStatusAttribute(unittest.TestCase):

    def test_when_status_is_not_set(self):
        obj = status.StatusHandler()
        obj.application = MockApplication()
        self.assertEqual(obj._application_status(), status.OK)

    def test_when_status_is_set_to_maintenance(self):
        obj = status.StatusHandler()
        obj.application = MockApplication()
        setattr(obj.application, 'status', status.MAINTENANCE)
        self.assertEqual(obj._application_status(), status.MAINTENANCE)


class TestStatusHandlerResponseCodes(unittest.TestCase):

    def test_when_status_is_not_set(self):
        obj = status.StatusHandler()
        obj.application = MockApplication()
        self.assertEqual(obj._status_response_code(), 200)

    def test_when_status_is_set_to_maintenance(self):
        obj = status.StatusHandler()
        obj.application = MockApplication()
        setattr(obj.application, 'status', status.MAINTENANCE)
        self.assertEqual(obj._status_response_code(), 503)

    def test_when_status_is_set_to_error(self):
        obj = status.StatusHandler()
        obj.application = MockApplication()
        setattr(obj.application, 'status','error')
        self.assertEqual(obj._status_response_code(), 500)
