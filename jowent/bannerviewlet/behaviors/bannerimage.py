# -*- coding: utf-8 -*-
from plone.app.contenttypes import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.directives import form
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements


class IBannerImage(model.Schema):

    form.order_before(banner_image='IDublinCore.description')
    banner_image = namedfile.NamedBlobImage(
        title=_(u"Banner Image"),
        description=u"",
        required=False,
    )

    form.order_before(banner_image_caption='IDublinCore.description')
    banner_image_caption = schema.TextLine(
        title=_(u"Banner Image Caption"),
        description=u"",
        required=False,
    )

alsoProvides(IBannerImage, IFormFieldProvider)


class BannerImage(object):
    implements(IBannerImage)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context
