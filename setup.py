from setuptools import setup, find_packages

setup(
    name='python-utils',
    version='0.1.0',  # TODO: Set your package's version number here
    author='Sisconsavior',
    author_email='aceliuchanghong@gmail.com',
    packages=find_packages(),
    url='https://github.com/aceliuchanghong/python-utils.git',
    license='LICENSE',  # TODO: If you have a license file, put its name here
    description='A collection of Python utilities for handling media files.',  # TODO: Write a short description here
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',  # TODO: Choose the Development Status
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',  # TODO: Choose your license
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',  # TODO: Specify the Python version requirements
    include_package_data=True,
    keywords='media handling image audio video conversion editing',  # TODO: Add some keywords for your package
    # TODO: Add any additional package data here
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.md', '*.txt'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },
    # TODO: Add any scripts or entry points here
    entry_points={
        'console_scripts': [
            'your_script = your_package.some_module:main_func',
        ],
    },
)
