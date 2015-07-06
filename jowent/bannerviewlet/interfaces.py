# -*- coding: utf-8 -*-
from jowent.bannerviewlet import MessageFactory as _
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class IBannerViewletInstalled(Interface):
    """ A layer specific for this add-on product.

    This interface is referred in browserlayer.xml.

    views and viewlets registered against this layer will appear on
    a Plone site only when the add-on installer has been run.
    """


policy_options = SimpleVocabulary(
    [
        SimpleTerm(value='exact', title=_(u'Exact - The supplied images must exactly match the Banner Height & Width specified below')),
        SimpleTerm(value='minimum', title=_(u'Minimum - An image with larger dimensions than below may be supplied, but it will be shrunk to the Banner Height & Width specified below')),
    ])

class IBannerViewletSettings(Interface):
    """Bannerviewlet settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    dimensions_policy = schema.Choice(
        title=_(u"Banner Validation Policy"),
        description=u"",
        vocabulary=policy_options,
        required=True,
    )
    required_height = schema.Int(title=_(u"Banner Height"),
                                 required=True,
                                 default=2000)

    required_width = schema.Int(title=_(u"Banner Width"),
                                required=True,
                                default=320)

    max_size = schema.Int(title=_(u"Maximum Filesize (in KB)"),
                          description=_(u"Leave this empty to stop filesize being checked"),
                          required=False,
                          default=200)
