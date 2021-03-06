import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-url-renditions',
    version='1.2',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Create custom renditions from django url fields',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/vied12/django-url-renditions',
    author='Edouard Richard',
    author_email='edou4rd@gmail.com',
    install_requires=['Pillow==5.1.0',],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
