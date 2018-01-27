from setuptools import setup

setup(
    name='meloshare',
    packages=['meloshare'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_flash'
    ],
)
