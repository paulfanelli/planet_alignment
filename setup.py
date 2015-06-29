import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Utility function to read the README file, used for the long desc.
def read(fn):
    return open(os.path.join(os.path.dirname(__file__), fn)).read()


setup(
    name='planet_alignment',
    version='1.0.0',
    packages=[
        'planet_alignment',
        'planet_alignment.app',
        'planet_alignment.cmd',
        'planet_alignment.config',
        'planet_alignment.data',
        'planet_alignment.mgr',
        'planet_alignment.plugins',
        'planet_alignment.test',
        'planet_alignment.utils'
    ],
    url='https://github.com/paulfanelli/planet_alignment.git',
    license='MIT',
    author='Paul Fanelli',
    author_email='paul.fanelli@gmail.com',
    description='Planet Alignment program',
    long_description=read('README'),
    install_requires=['bunch', 'zope.interface', 'PyYAML'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'planet_alignment = planet_alignment.__main__:main'
        ]
    },
    include_package_data=True
)
