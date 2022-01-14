from setuptools import setup, find_packages

VERSION = (0, 3, 2)
__version__ = '.'.join(map(str, VERSION))

setup(
    name='django-map-widgets',
    version=__version__,
    description='Map widgets for Django PostGIS fields',
    long_description='Configurable, pluggable and more user friendly map widgets for Django PostGIS fields.',
    long_description_content_type='text/x-rst',
    author='Edgar Ramirez',
    author_email='edario.ram.le@gmail.com',
    url='https://github.com/EDario333/django-map-widgets',
    license='MIT',
    platforms=['any'],
    packages=find_packages(exclude=('example', 'static', 'env')),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
)

