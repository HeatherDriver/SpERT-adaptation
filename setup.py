from glob import glob
from setuptools import find_packages, setup

types = ('*.json', '*.bin', '*txt')
data_files = []
for t in types:
    data_files.extend(glob('spert/data/**/' + t, recursive=True))

setup(
    name='spert',
    packages=find_packages(),
    data_files=[('config', ['spert/configs/eval.cfg', 'spert/configs/train.cfg']),
                ('data', data_files)],
    package_data={'': ['*.json'], '': ['*.bin', '*.txt']},
    include_package_data=True,
    version='1.0.0',
    description='spert',
    author='Me',
    license='MIT',
)