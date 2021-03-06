# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from jowent.bannerviewlet.interfaces import IBannerViewletSettings
from jowent.bannerviewlet.testing import JOWENT_BANNERVIEWLET_INTEGRATION_TESTING  # noqa
from plone import api
from plone.registry import Registry

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that configuration for the product can be set & read."""

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

    def test_setting_validation_policy(self):
        """Test that the validation_policy record is in our control panel"""
        validation_policy = self.registry.records[
            'jowent.bannerviewlet.interfaces.IBannerViewletSettings.validation_policy']
        self.failUnless('validation_policy' in IBannerViewletSettings)
        self.assertEquals(validation_policy.value, 'exact')

    def test_setting_undersized_banner_behavior(self):
        """Test that the undersized_banner_behavior record is in our control panel"""
        undersized_banner_behavior = self.registry.records[
            'jowent.bannerviewlet.interfaces.IBannerViewletSettings.undersized_banner_behavior']
        self.failUnless('undersized_banner_behavior' in IBannerViewletSettings)
        self.assertEquals(undersized_banner_behavior.value, 'centred')

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
        """Test that the max_filesize record is in our control panel"""
        max_filesize = self.registry.records[
            'jowent.bannerviewlet.interfaces.IBannerViewletSettings.max_filesize']
        self.failUnless('max_filesize' in IBannerViewletSettings)
        self.assertEquals(max_filesize.value, 200)

    @unittest.skip("not yet implemented")
    def test_actually_setting(self):
        pass
