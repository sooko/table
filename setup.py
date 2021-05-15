from setuptools import setup, find_packages

setup(
name='table',
version='0.1.0',
author='An Awesome Coder',
author_email='aac@example.com',
packages=['table'],
package_data= {
        'table': ['*.kv'],
    },
url='https://github.com/sooko/table.git',
license='LICENSE.txt',
description='An awesome package that does something',
long_description='An awesome package that does something',
include_package_data=True,
install_requires=[
],)