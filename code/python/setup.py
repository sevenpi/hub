from setuptools import setup, find_packages

author   = 'Clement Wong'
email    = 'sevenpi.883@gmail.com'
version  = '0.0.1'
scripts  = []
exclude  = []
requires = []

setup(
    name                 = 'Copper',
    description          = 'Data Analysis',
    version              = version,
    author               = author,
    author_email         = email,
    license              = 'LICENSE',
    long_description     = open( 'README' ).read(),
    packages             = find_packages( exclude=exclude ),
    scripts              = scripts,
    install_requires     = requires,
    include_package_data = True,
    zip_safe             = True,
)

