from setuptools import find_packages, setup

setup(
    name='spert',
    packages=find_packages(),
    package_data={'json': ['*.json'],
                  'config': ['*.cfg']},
    include_package_data=True,
    version='1.0.0',
    description='spert',
    author='Me',
    license='MIT',
)