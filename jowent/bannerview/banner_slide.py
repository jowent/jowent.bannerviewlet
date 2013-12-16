from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from jowent.bannerview import MessageFactory as _


# Interface class; used to define content-type schema.

class IBannerSlide(form.Schema, IImageScaleTraversable):
    """
    An image that will be displayed in the BannerViewlet as part of a slideshow
    """

    # field defintions go here


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class BannerSlide(Container):
    grok.implements(IBannerSlide)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# banner_slide_templates.
# Template filenames should be all lower case.

class View(grok.View):
    """ standard view class """

    grok.context(IBannerSlide)
    grok.require('zope2.View')

    # Add view methods here
