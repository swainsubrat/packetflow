from setuptools import setup

classifiers = []

setup(
    name='packetflow',
    version='0.0.1',
    description='A Library for adversarial attacks and defences on IDS',
    long_description=open("README.md").read() + '\n\n' + open("CHANGELOG.txt").read(),
    url='https://github.com/swainsubrat/packetflow',
    author='Subrat Kumar',
    author_email='mailofswainsubrat@gmail.com',
    license='MIT',
    # classifiers=classifiers,
    keywords='ids adversarial network',
    packages=['packetflow'],
    install_requires=[''],
    zip_safe=False
)