import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='mcapy',
    version='0.9.0',
    author='wensheng',
    description='A Minecraft MCA file reader/writer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wensheng/mcapy',
    packages=['mca'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[],
    include_package_data=True
)
