# -*- coding: utf-8 -*-
from jowent.bannerviewlet.interfaces import IBannerViewletSettings
from jowent.bannerviewlet import MessageFactory as _
from plone.app.registry.browser import controlpanel


class BannerViewletSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IBannerViewletSettings
    label = _(u"Banner Viewlet Settings")
    description = _(u"""    These settings control the permitted dimensions and filesize of the BannerViewlet (and the Banner Images which are used to fill it).

    Note that changing the dimensions settings will resize the BannerViewlet, but it will NOT resize existing Banner Images.
    Depending on which way you are resizing this could result in:
        a) smaller images looking blurry when stretched to match dimensions
        b) blank space to the side of images when height/width ratio changes
        c) larger images taking more diskspace/memory than they need to
    These issues can be resolved by simply updating all Banner Images across your site.
    """)

    def updateFields(self):
        super(BannerViewletSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(BannerViewletSettingsEditForm, self).updateWidgets()

class BannerViewletSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = BannerViewletSettingsEditForm
