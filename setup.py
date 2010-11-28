import os
from setuptools import setup, find_packages

version = '1.6.0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read() + '\n\n'

long_description = (
    """
===================
PloneSoftwareCenter
===================

""" + 
    read('README.txt')+
    read('docs', 'INSTALL.txt')+
    read('docs', 'HISTORY.txt')
)

description =  """\
PloneSoftwareCenter is a tool that keeps track of software projects.
"""

setup(name='Products.PloneSoftwareCenter',
      version=version,
      description=description,
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Plone Website Team',
      author_email='plone-website@lists.sourceforge.net',
      maintainer='Alex Clark',
      maintainer_email='aclark@aclark.net',
      url='http://plone.org/products/plonesoftwarecenter',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'contentratings',
          'setuptools',
          'Products.ArchAddOn',
          'Products.AddRemoveWidget',
          'Products.DataGridField',
          'collective.fancyzoomview',
          'plone.contentratings',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

