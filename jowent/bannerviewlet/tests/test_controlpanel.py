# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from jowent.bannerviewlet.interfaces import IBannerViewletSettings
from jowent.bannerviewlet.testing import JOWENT_BANNERVIEWLET_INTEGRATION_TESTING  # noqa
from plone import api
from plone.registry import Registry

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that jowent.bannerviewlet is properly installed."""

    layer = JOWENT_BANNERVIEWLET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.registry = Registry()
        self.registry.registerInterface(IBannerViewletSettings)

    def test_controlpanel_view(self):
        """Test the controlpanel is visible."""
        from zope.component import getMultiAdapter
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name="bannerviewlet-settings")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_controlpanel_view_protected(self):
        """Test that the control panel view is protected and anonymous users can't view or edit it."""
        from AccessControl import Unauthorized
        from plone.app.testing import logout
        portal = self.layer['portal']
        logout()
        self.assertRaises(Unauthorized,
                          self.portal.restrictedTraverse,
                         '@@bannerviewlet-settings')

    def test_setting_dimensions_policy(self):
        """Test that the dimensions_policy record is in our control panel"""
        dimensions_policy = self.registry.records[
            'jowent.bannerviewlet.interfaces.IBannerViewletSettings.dimensions_policy']
        self.failUnless('dimensions_policy' in IBannerViewletSettings)
        self.assertEquals(dimensions_policy.value, 'exact')

    def test_setting_required_height(self):
        """Test that the required_height record is in our control panel"""
        required_height = self.registry.records[
            'jowent.bannerviewlet.interfaces.IBannerViewletSettings.required_height']
        self.failUnless('required_height' in IBannerViewletSettings)
        self.assertEquals(required_height.value, 320)

    def test_setting_required_width(self):
        """Test that the required_width record is in our control panel"""
        required_width = self.registry.records[
            'jowent.bannerviewlet.interfaces.IBannerViewletSettings.required_width']
        self.failUnless('required_width' in IBannerViewletSettings)
        self.assertEquals(required_width.value, 2000)

    def test_setting_max_filesize(self):
        """Test that the max_size record is in our control panel"""
        max_filesize = self.registry.records[
            'jowent.bannerviewlet.interfaces.IBannerViewletSettings.max_filesize']
        self.failUnless('max_filesize' in IBannerViewletSettings)
        self.assertEquals(max_filesize.value, 200)
