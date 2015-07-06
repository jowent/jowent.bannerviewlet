# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import jowent.bannerviewlet


class BorgPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=jowent.bannerviewlet)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'jowent.bannerviewlet:default')

JOWENT_BANNERVIEWLET_FIXTURE = BorgPolicyLayer()


JOWENT_BANNERVIEWLET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(JOWENT_BANNERVIEWLET_FIXTURE,),
    name='JowentBannerviewletLayer:IntegrationTesting'
)


JOWENT_BANNERVIEWLET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(JOWENT_BANNERVIEWLET_FIXTURE,),
    name='JowentBannerviewletLayer:FunctionalTesting'
)


JOWENT_BANNERVIEWLET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        JOWENT_BANNERVIEWLET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='JowentBannerviewletLayer:AcceptanceTesting'
)
