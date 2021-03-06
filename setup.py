import codecs
import setuptools

setuptools.setup(
    name='sprockets.handlers.status',
    version='0.1.2',
    description='A small handler for reporting application status',
    long_description=codecs.open('README.rst', 'r', 'utf8').read(),
    url='https://github.com/sprockets/sprockets.handlers.status',
    author='AWeber Communications',
    author_email='api@aweber.com',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=['sprockets',
              'sprockets.handlers',
              'sprockets.handlers.status'],
    package_data={'': ['LICENSE', 'README.md']},
    include_package_data=True,
    install_requires=['tornado'],
    namespace_packages=['sprockets',
                        'sprockets.handlers'],
    zip_safe=False)
