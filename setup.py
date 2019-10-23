try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'SSH Observatory',
    'author': 'Jonathan Claudius',
    'url': '',
    'download_url': '',
    'author_email': 'jclaudius@mozilla.com',
    'version': "0.0.1",
    'install_requires': ['requests'],
    'packages': ['scans'],
    'scripts': [],
    'data_files': [],
    'name': 'scans'
}

setup(**config)
