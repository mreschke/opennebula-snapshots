# Tutorial https://python-packaging.readthedocs.io/en/latest/minimal.html

from setuptools import setup

setup(
    name='mreschke-opennebula-snapshots',
    version='1.0.0',
    description='KVM Live Qcow2 Snapshots using Libvirt',
    long_description='',

    author='Matthew Reschke',
    author_email='mail@mreschke.com',
    license='MIT',
    url='http://github.com/mreschke/kvmsnapshots',

    # I am using "Native namespaces" see https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages
    packages=['mreschke.opennebula_snapshots'],
    zip_safe=False,
    python_requires='>=3.7',
    #install_requires=[
    #    'click'
    #],
    entry_points={
        'console_scripts': [
            'opennebula-snapshots=mreschke.opennebula_snapshots.cli:cli'
        ],
    },
)

