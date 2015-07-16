# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from jowent.bannerviewlet.testing import JOWENT_BANNERVIEWLET_INTEGRATION_TESTING  # noqa
from jowent.bannerviewlet.banner_slide import IBannerSlide

import unittest2 as unittest


class BannerSlideIntegrationTest(unittest.TestCase):
    """Test that bannerslide type can be added, edited and viewed."""

    layer = JOWENT_BANNERVIEWLET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        """Test that FTI type returns object with the correct schema"""
        fti = queryUtility(IDexterityFTI, name='jowent.bannerviewlet.bannerslide')
        schema = fti.lookupSchema()
        self.assertEqual(IBannerSlide, schema)

    def test_fti(self):
        """Test that FTI type returns object of requested type"""
        fti = queryUtility(IDexterityFTI, name='jowent.bannerviewlet.bannerslide')
        self.assertTrue(fti)

    def test_factory(self):
        """Test that factory creates an object with the correct schema"""
        fti = queryUtility(IDexterityFTI, name='jowent.bannerviewlet.bannerslide')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IBannerSlide.providedBy(obj))

    def test_adding(self):
        """Test that adding through invokeFactory returns object with correct schema"""
        self.portal.invokeFactory('jowent.bannerviewlet.bannerslide', 'new-banner-slide')
        self.assertTrue(
            IBannerSlide.providedBy(self.portal['new-banner-slide'])
        )
