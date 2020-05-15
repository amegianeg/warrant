from setuptools import setup, find_packages


version = '0.6.1'

README = """Python class to integrate Boto3's Cognito client so it is easy to login users. With SRP support."""


with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('requirements_test.txt', 'r') as f:
    test_requirements = f.read().splitlines()

setup(
    name='warrant',
    version=version,
    description=README,
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
    keywords='aws,cognito,api,gateway,capless',
    author='Capless.io',
    author_email='opensource@capless.io',
    maintainer='Brian Jinwright',
    packages=find_packages(),
    url='https://github.com/capless/warrant',
    license='Apache License 2.0',
    install_requires=requirements,
    extras_require={'test': test_requirements},
    include_package_data=True,
    zip_safe=True,

)
