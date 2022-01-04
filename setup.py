from setuptools import setup, find_packages


def get_dependencies():
    return [
        'Marshmallow',
    ]


setup(
    name='PF-Flask-Rest-Com',
    version='1.0.0',
    url='https://github.com/problemfighter/pf-flask-rest-com',
    license='Apache 2.0',
    author='Problem Fighter',
    author_email='problemfighter.com@gmail.com',
    description='Flask REST API Common Implementation by Problem Fighter Library',
    long_description=__doc__,
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