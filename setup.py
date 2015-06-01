import setuptools
import sys

tests_require = [line.strip() for line in open('test-requirements.txt', 'r')]
if sys.version_info < (2, 7):
    tests_require.append('unittest2')
if sys.version_info < (3, 0):
    tests_require.append('mock')

setuptools.setup(
    name='sprockets.handlers.status',
    version='0.1.0',
    description='A small handler for reporting application status',
    long_description=open('test-requirements.txt', 'r').read(),
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
    package_data={'': ['LICENSE', 'README.md', 'test-requirements.txt']},
    include_package_data=True,
    namespace_packages=['sprockets',
                        'sprockets.handlers'],
    tests_require=tests_require,
    zip_safe=False)
