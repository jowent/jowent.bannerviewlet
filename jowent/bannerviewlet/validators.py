# -*- coding: utf-8 -*-
from five import grok
from jowent.bannerviewlet import MessageFactory as _
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
            if (width != settings.required_width or
                height != settings.required_height):
                raise Invalid(_(u"image_wrong_dimensions",
                        default=u"Image has wrong dimensions - it should be ${required_height} x ${required_width} pixels (h x w)"
                              ", but is ${actual_height} x ${actual_width}",
                        mapping={"required_height": settings.required_height,
                                 "required_width": settings.required_width,
                                 "actual_height": height,
                                 "actual_width": width}))

            # Lastly check filesize
            if value.getSize() > (settings.max_filesize * 1024):
                raise Invalid(_(u"image_too_large",
                            default=u"Image filesize is too large. Maximum permitted: ${max_filesize}KB",
                            mapping={"max_filesize": settings.max_filesize}))


validator.WidgetValidatorDiscriminators(ImageDimensionsValidator,
                                        context=IBannerImage,
                                        field=IBannerImage['banner_image'])
grok.global_adapter(ImageDimensionsValidator)
