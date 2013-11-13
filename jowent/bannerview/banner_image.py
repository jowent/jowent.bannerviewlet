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

class IBannerImage(form.Schema, IImageScaleTraversable):
    """
    An image that will be displayed in the Banner Viewlet for it's folder, 
    or any contained content that does not have a Lead Image set
    """

    # We want a model-based interface, edit
    # models/banner_image.xml to define the content type.

    form.model("models/banner_image.xml")


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class BannerImage(Container):
    grok.implements(IBannerImage)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# banner_image_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IBannerImage)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
