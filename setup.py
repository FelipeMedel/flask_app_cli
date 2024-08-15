from setuptools import setup, find_packages

readme = open('./README.md', 'r')

setup(
    name='flask_app_cli',
    version='0.0.1',
    description='Generador de proyectos de Python con Flask',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Felipe Medel',
    author_email='luispipemedel@gmail.com',
    packages=find_packages(),
    py_modules=['main'],
    install_requires=['click', 'colorama'],
    keywords=['flask', 'flask-cli', 'flask-app-cli', 'generate flask app'],
    license='MIT',
    include_package_data=True,
)
