# -*- coding: utf-8 -*-
from plone.namedfile.interfaces import INamedBlobImageField
from plone.app.contenttypes.behaviors.leadimage import ILeadImage
from plone.app.contenttypes.interfaces import INewsItem

from zope.interface import Invalid
from z3c.form import validator
from five import grok

# Strict Dimensions check
REQUIRED_HEIGHT = 320
REQUIRED_WIDTH = 2000

# Filesize limit
MAXSIZE_KB = 200


class ImageDimensionsValidator(validator.FileUploadValidator):

    def validate(self, value):
        super(ImageDimensionsValidator, self).validate(value)

        if INewsItem.providedBy(value):
            return None

        if value:
            # See: plone.namedfile.file.NamedBlobImage
            width, height = value.getImageSize()
            
            if REQUIRED_HEIGHT and REQUIRED_WIDTH:
                if (width != REQUIRED_WIDTH or
                    height != REQUIRED_HEIGHT):
                    raise Invalid("Image has wrong dimensions - it should be %d x %d pixels (h x w)"
                                  ", but is %d x %d" %
                                  (REQUIRED_HEIGHT, REQUIRED_WIDTH, height, width))
            elif REQUIRED_HEIGHT:
                if (height != REQUIRED_HEIGHT):
                    raise Invalid("Image is the wrong height - it should be %d pixels" %
                                  (REQUIRED_HEIGHT))
            elif REQUIRED_WIDTH:
                if (width != REQUIRED_WIDTH):
                    raise Invalid("Image is the wrong width - it should be %d pixels" %
                                  (REQUIRED_WIDTH))

            # Lastly check filesize
            if value.getSize() > (MAXSIZE_KB * 1024):
                raise Invalid("Image filesize is too large. Maximum permitted: %dKB " % MAXSIZE_KB)
            


validator.WidgetValidatorDiscriminators(ImageDimensionsValidator,
                                        context=ILeadImage,
                                        field=ILeadImage['image'])
grok.global_adapter(ImageDimensionsValidator)
