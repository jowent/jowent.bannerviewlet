# -*- coding: utf-8 -*-
from five import grok
from jowent.bannerviewlet.behaviors.bannerimage import IBannerImage
from jowent.bannerviewlet.interfaces import IBannerViewletSettings
from plone.namedfile.interfaces import INamedBlobImageField
from plone.registry.interfaces import IRegistry
from z3c.form import validator
from zope.component import getUtility
from zope.interface import Invalid


class ImageDimensionsValidator(validator.FileUploadValidator):

    def validate(self, value):
        super(ImageDimensionsValidator, self).validate(value)

        if value:
            # See: plone.namedfile.file.NamedBlobImage
            width, height = value.getImageSize()

            registry = getUtility(IRegistry)
            settings = registry.forInterface(IBannerViewletSettings)

            # For the time being, ignore settings.validation_policy and
            # go with an *exact* Dimensions check
            if settings.required_height and settings.required_width:
                if (width != settings.required_width or
                    height != settings.required_height):
                    raise Invalid("Image has wrong dimensions - it should be %d x %d pixels (h x w)"
                                  ", but is %d x %d" %
                                  (settings.required_height, settings.required_width, height, width))
            elif settings.required_height:
                if (height != settings.required_height):
                    raise Invalid("Image is the wrong height - it should be %d pixels" %
                                  (settings.required_height))
            elif settings.required_width:
                if (width != settings.required_width):
                    raise Invalid("Image is the wrong width - it should be %d pixels" %
                                  (settings.required_width))

            # Lastly check filesize
            if value.getSize() > (settings.max_filesize * 1024):
                raise Invalid("Image filesize is too large. Maximum permitted: %dKB " % settings.max_filesize)


validator.WidgetValidatorDiscriminators(ImageDimensionsValidator,
                                        context=IBannerImage,
                                        field=IBannerImage['banner_image'])
grok.global_adapter(ImageDimensionsValidator)
