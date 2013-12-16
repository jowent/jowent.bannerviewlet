# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase

from plone.app.contenttypes.interfaces import INewsItem
from jowent.bannerview.behaviors.bannerimage import IBannerImage
from jowent.bannerview.banner_slide import IBannerSlide

from Products.CMFCore.interfaces import IFolderish
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.CMFCore.utils import getToolByName

import logging

logger = logging.getLogger('jowent.bannerviewlet')


class BannerViewlet(ViewletBase):
    """ 
    A viewlet which renders a banner according to the following conditions:
        - if a BannerImage is set on the content item then render that image
        - if the content item is not folderish and a BannerImage is set on it's
            parent folder then render that image
        - if any folder among the content items parents (including itself if it's a folder)
            contains just one published BannerSlide then render that as a still image
        - if any folder among the content items parents (including itself if it's a folder)
            contains multiple published BannerSlides then them as a slideshow
            (ordered by their position in the folder)
        - if none of the above apply then render an empty viewlet 
            (which may have height if CSS enforces it)
    """

    def update(self):

        logger.info("starting banner search at %s " % self.context )
        if IFolderish.providedBy(self.context):
            logger.info("findBannerImageFor(self) %s " % self.context )
            self.findBannerImageFor(self.context)
        else:
            if IBannerImage.providedBy(self.context):
                banner = IBannerImage(self.context)
                if banner.banner_image:
                    logger.info("context has banner_image")
                    self.banners = [banner]
                    self.available = True
                    return 
                    
            #parent = self.context.aq_parent
            parent = self.context.aq_parent
            logger.info("findBannerImageFor(parent) %s " % parent )
            self.findBannerImageFor(parent)
                


    def findBannerImageFor(self, folder):
        """Find the banner image to be displayed in a folder"""
        
        # First see if the banner is defined by the folder
        if IBannerImage.providedBy(folder):
            banner = IBannerImage(folder)
            if banner.banner_image:
                logger.info("banner_image defined by folder")
                self.banners = [banner]
                self.available = True
                return 
        
        
        # Next check for (possibly multiple) banner(s) in the folder
        # and return them all
        path = folder.getPhysicalPath()
        path = "/".join(path)

        #catalog = getToolByName(self.context, 'portal_catalog')
        logger.info("getting portal catalog")
        catalog = self.context.portal_catalog
        logger.info("searching portal catalog")
        brains = catalog(path={"query": path, "depth": 1}, 
                         object_provides=IBannerSlide.__identifier__,
                         review_state="published",
                         sort_on="getObjPositionInParent")
        if brains:
            self.banners = []
            for brain in brains:
                obj = brain.getObject()
                if obj.banner_image:
                    self.banners.append(obj)
            logger.info("got portal catalog %s" % self.banners)
            if self.banners:
                self.available = True
                return
        
        
        # Lastly check the parent (unless this is the navigation root)
        if not INavigationRoot.providedBy(folder):
            #parent = folder.aq_parent
            parent = folder.aq_parent
            logger.info("check parent - findBannerImageFor(parent) %s " % parent )
            self.findBannerImageFor(parent)
        else:
            # Otherwise - we searched all the way to the nav root & found nothing
            logger.info("At root - found nothing")
            self.available = False


