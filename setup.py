import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ckeditor-widget',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD-3 License',
    description='A CKEditor widget for Django that includes an admin mixin.',
    long_description=README,
    url='https://github.com/Wtower/django-ckeditor-widget',
    author='George Karakostas',
    author_email='gckarakostas@gmail.com',
    keywords='django ckeditor widget',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
