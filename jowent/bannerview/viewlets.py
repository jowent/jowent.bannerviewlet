# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase

from plone.app.contenttypes.interfaces import INewsItem
from plone.app.contenttypes.behaviors.leadimage import ILeadImage

#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from archetype.KHLaw.interfaces import IDefinesBanner, IBannerImage


class BannerViewlet(ViewletBase):
    """ 
    A viewlet which renders a banner according to the following conditions:
        - if a leadimage is set on the content item then render that image
        - if the content item is not folderish and a leadimage is set on it's
            parent folder then render that image
        - if the nearest folderish item (either the content itself, or it's 
            parent) contains just one published BannerImage then render that
        - if the nearest folderish item contains multiple published BannerImages
            then render them as a slideshow
    """

    def update(self):

        if ILeadImage.providedBy(self.context):
            self.context = ILeadImage(self.context)
            self.available = True if self.context.image else False
            #if INewsItem.providedBy(self.context):
                #self.available = False
        else:
            self.available = False



    def khlaw_update(self):
        super(ViewletBase, self).update()

        context = self.context

        bannerimage = getattr(context, 'bannerimage', None)

        if IDefinesBanner.providedBy(context) and bannerimage:
            self.banner_tag = bannerimage.tag()
        else:
            defaultbanner = context.restrictedTraverse('defaultbanner', None)
            if defaultbanner is not None and IBannerImage.providedBy(defaultbanner):
                self.banner_tag = defaultbanner.tag()
            else:
                self.banner_tag = ''
