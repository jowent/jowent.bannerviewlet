# -*- coding: utf-8 -*-
from jowent.bannerviewlet.interfaces import IBannerViewletSettings
from jowent.bannerviewlet import MessageFactory as _
from plone.app.registry.browser import controlpanel


class BannerViewletSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IBannerViewletSettings
    label = _(u"Banner Viewlet Settings")
    description = _(u"""These settings control the dimensions of the BannerViewlet,
            and the permitted dimensions and filesize of the Banner Slides which
            are used to fill it. &nbsp;&nbsp;
            Note that changing these dimensions will <b>NOT</b> revalidate or resize
            any existing Banner Slides.""")

    def updateFields(self):
        super(BannerViewletSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(BannerViewletSettingsEditForm, self).updateWidgets()

class BannerViewletSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = BannerViewletSettingsEditForm
