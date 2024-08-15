from setuptools import setup, find_packages

readme = open('./README.md', 'r')

VERSION = '0.0.1'
DESCRIPTION = 'Generador de proyectos de Python utilizando el framework Flask, por medio de la terminal.'
PACKAGE_NAME = 'Package Name'
AUTHOR = 'Felipe Medel'
EMAIL = 'luispipemedel@gmail.com'
GITHUB_URL = ''

setup(
    name='flask_app_cli',
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(),
    py_modules=['main'],
    install_requires=['click', 'colorama'],
    keywords=['flask', 'flask-cli', 'flask-app-cli', 'generate flask app'],
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',  # Estados del paquete "3 - Alpha", "4 - Beta", "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
