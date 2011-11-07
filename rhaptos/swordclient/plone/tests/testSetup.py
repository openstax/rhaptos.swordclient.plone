import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from base import PROJECTNAME
from base import INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testToolInstalled(self):
        tool = getToolByName(self.portal, 'sword_repositories_tool')
        assert tool.id == 'sword_repositories_tool', tool.id
        assert tool.meta_type == 'Sword Repositories Tool', tool.meta_type

class TestReinstall(unittest.TestCase):
    """Ensure product can be reinstalled safely"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testReinstall(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')
        try:
            portal_setup.runAllImportStepsFromProfile('profile-%s:default' % PROJECTNAME)
        except BadRequest:
            # if tests run too fast, duplicate profile import id makes test fail
            time.sleep(0.5)
            portal_setup.runAllImportStepsFromProfile('profile-%s:default' % PROJECTNAME)
