from setuptools import setup, find_packages

setup(
    name='django-taggit-tokenfield',
    version='1.0',
    description='Autocompleting, tokenizing widget for django-taggit.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django >=1.4',
        'django-taggit',
    ]
)
