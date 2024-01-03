# setup.py

from setuptools import setup, find_packages

setup(
    name='python_utils',
    version='0.1.0',
    author='Sisconsavior',
    author_email='aceliuchanghong@gmail.com',
    packages=find_packages(),
    url='https://github.com/aceliuchanghong/python-utils.git',
    license='LICENSE',
    description='An utility package for usua program processing.',
    long_description=open('README.md').read(),
    install_requires=[
        # 添加你的包依赖的其他Python包列表
        # 例如:
        # 'moviepy>=1.0.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            # 如果你的包提供了一个或多个脚本，可以在这里添加
            # 例如:
            # 'mp4_to_gif=mp4_utils.converters.mp4_to_gif:main',
        ],
    },
)
