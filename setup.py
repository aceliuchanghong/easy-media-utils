from setuptools import setup, find_packages

setup(
    name='easy-media-utils',
    version='0.1.5',  # Update the version number for new releases
    author='Sisconsavior',
    author_email='aceliuchanghong@gmail.com',
    packages=find_packages(),
    url='https://github.com/aceliuchanghong/easy-media-utils.git',
    license='LICENSE',  # If you have a license file, specify its name here, e.g., 'LICENSE.txt'
    description='A collection of Python utilities for handling media files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',  # Update the development status as appropriate
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',  # Update the license if it's not MIT
        'Programming Language :: Python :: 3.11',  # Update if you support other Python versions
    ],
    python_requires='>=3.6',  # Update the Python version requirements if necessary
    include_package_data=True,
    keywords='media handling image audio video conversion editing',  # Add any keywords relevant to your package
    package_data={
        # Include Markdown, text files, and message files from any package
        '': ['*.md', '*.txt', '*.msg'],
        # Include any other data files you may have, like test files or data samples
        'testfiles': ['*.mkv', '*.mp4'],
    },
    entry_points={
        'console_scripts': [
            # Replace 'your_script' with your script's name and 'your_package.some_module:main_func'
            # with the path to your package's main function.
            'print_tree = tests.struct_tree_out:print_tree',
        ],
    },
    # Ensure that non-code files inside your package folders are included (like *.md, *.txt)
    # If you have other types of files like templates, include them as well
    zip_safe=False  # Set to False if you will be including non-code files
)

# Note: You should create MANIFEST.in file to include other types of files like .md and .txt
# conda install setuptools wheel twine
# python setup.py sdist bdist_wheel
# twine upload dist/*
