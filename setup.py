from distutils.core import setup

setup(
    name='planet_alignment',
    version='1.0.0',
    packages=['planet_alignment', 'planet_alignment.test'],
    url='https://github.com/paulfanelli/planet_alignment.git',
    license='MIT',
    author='Paul Fanelli',
    author_email='paul.fanelli@gmail.com',
    description='Planet Alignment program',
    requires=['bunch', 'zope.interface', 'PyYAML'],
    tests_require=['pytest']
)
