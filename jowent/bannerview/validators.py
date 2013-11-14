# -*- coding: utf-8 -*-
from plone.namedfile.interfaces import INamedBlobImageField
# from plone.app.contenttypes.interfaces import IImage
from zope.interface import Invalid
from z3c.form import validator
from five import grok

# 1 MB size limit
MAXSIZE = 1024 * 1024


class ImageDimensionsValidator(validator.FileUploadValidator):

    def validate(self, value):
        super(ImageDimensionsValidator, self).validate(value)

        if value.getSize() > MAXSIZE:
            raise Invalid("Image is too large (too many bytes)")


validator.WidgetValidatorDiscriminators(ImageDimensionsValidator,
#                                        context=IImage,
                                        field=INamedBlobImageField)
grok.global_adapter(ImageDimensionsValidator)
