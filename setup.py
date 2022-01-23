import os

from setuptools import setup, find_packages
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent
README = (CURRENT_DIR / "readme.md").read_text()

env = os.environ.get('source')


def get_dependencies():
    dependency = [
        'Flask',
        'Marshmallow',
    ]

    if env and env == "dev":
        return dependency

    return dependency + ["PF-PY-Common"]


setup(
    name='PF-Flask-Rest-Com',
    version='1.0.2',
    url='https://github.com/problemfighter/pf-flask-rest-com',
    license='Apache 2.0',
    author='Problem Fighter',
    author_email='problemfighter.com@gmail.com',
    description='Flask REST API Common Implementation by Problem Fighter Library',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_dependencies(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)