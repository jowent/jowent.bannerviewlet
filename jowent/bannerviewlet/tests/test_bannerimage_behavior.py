# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from jowent.bannerviewlet.testing import JOWENT_BANNERVIEWLET_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that bannerimage behavior adds elements to types it is applied to."""

    layer = JOWENT_BANNERVIEWLET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_placeholder(self):
        """Test if something or other."""
        self.assertTrue(self.installer.isProductInstalled('jowent.bannerviewlet'))
