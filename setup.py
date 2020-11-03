from setuptools import find_packages, setup

setup(
    name='spert',
    packages=find_packages(),
    data_files=[('data', ['*.json', '*.conf'])],
    package_data={'config': []},
    include_package_data=True,
    version='1.0.0',
    description='spert',
    author='Me',
    license='MIT',
)