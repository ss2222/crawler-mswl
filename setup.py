'''
Created on 27/09/2012

Setuptools setup file

@author: ricardo
'''
 
from setuptools import setup, find_packages

setup (name="ricardo-crawler",
        version="0.1",
        packages=find_packages(),
        scripts=['ricardo-crawler'],
        install_requires=['BeautifulSoup'],
        package_data={'pyricardo-crawler':[''], },
        author='Ricardo García Fernández',
        author_email='ricardogarfe@gmail.com',
        description='My first Web Scrapper in Python',
        license='',
        keywords='',
        url='',
        long_description='',
        download_url='',
        )