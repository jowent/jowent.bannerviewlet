# -*- coding: utf-8 -*-
from jowent.bannerviewlet.interfaces import IBannerViewletSettings
from jowent.bannerviewlet import MessageFactory as _
from plone.app.registry.browser import controlpanel


class BannerViewletSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IBannerViewletSettings
    label = _(u"Banner Viewlet Settings")
    description = _(u"""These settings control the permitted dimensions and filesize
    of the Banner Images which are used to fill the BannerViewlet.
    """)

    def updateFields(self):
        super(BannerViewletSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(BannerViewletSettingsEditForm, self).updateWidgets()

class BannerViewletSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = BannerViewletSettingsEditForm
