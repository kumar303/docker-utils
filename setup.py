from setuptools import setup


setup(
    name='docker-utils',
    version='0.1',
    description='Utilities for Docker',
    long_description=open('README.rst').read(),
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    install_requires=['requests', 'Flask', 'docker-compose'],
    packages=['docker_utils'],
    url='https://github.com/andymckay/docker-utils',
    zip_safe=True,
)
