# -*- coding: utf-8 -*-
""" Browser layer interface for this add-on.
"""

import zope.interface

class IBannerViewletInstalled(zope.interface.Interface):
    """ A layer specific for this add-on product.

    This interface is referred in browserlayer.xml.

    views and viewlets registered against this layer will appear on
    a Plone site only when the add-on installer has been run.
    """
