import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='carrier_client',
      version='0.2',
      description='Carrier client',
      packages=find_packages(),
      url='https://github.com/EduScaled/carrier-client',
      author='Nick Lubyanov',
      author_email='lubyanov@gmail.com',
      license='MIT',
      install_requires=['requests', 'jsonschema', 'strict-rfc3339'],
      include_package_data=True,
      zip_safe=False)
