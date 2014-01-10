from setuptools import setup, find_packages
import os

version = '0.6'

setup(name='jowent.bannerviewlet',
      version=version,
      description="Banner/Slideshow Viewlet",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone, Banner, Viewlet, Carousel, plone.app.contenttypes',
      author='Daniel Jowett',
      author_email='daniel@jowettenterprises.com',
      url='http://www.jowettenterprises.com/products/bannerviewlet/',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['jowent'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
          'plone.behavior',
          'plone.directives.form',
          'zope.schema',
          'zope.interface',
          'zope.component',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
