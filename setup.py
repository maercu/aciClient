from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='aciClient',
      version='1.6',
      description='aci communication helper class',
      url='http://www.netcloud.ch',
      author='Netcloud AG',
      author_email='nc_dev@netcloud.ch',
      license='MIT',
      packages=['aciClient'],
      install_requires=['requests[socks]>=2.26.0 , <3', 'pyOpenSSL>=23.0.0, <26', 'PySocks>=1.7.1, <2'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      python_requires=">=3.6",
      zip_safe=False)
