from setuptools import find_packages, setup

setup(
    name='dicepy',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 
        'marshmallow',
        'mysql-connector-python',
        'openpyxl',
        'pandas',
        'python-dotenv'
    ]
)
