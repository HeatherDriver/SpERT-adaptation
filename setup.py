from setuptools import find_packages, setup

setup(
    name='spert',
    packages=find_packages(),
    data_files=[('config', ['spert/configs/eval.cfg', 'spert/configs/train.cfg'])],
                # ('datasets', [])],
    package_data={'json': ['*.json'], 'models': ['*.bin', '*.txt']},
    include_package_data=True,
    version='1.0.0',
    description='spert',
    author='Me',
    license='MIT',
)