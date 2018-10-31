from setuptools import setup, find_packages

setup(name='carrier_client',
      version='0.2',
      description='Carrier client',
      packages=find_packages(),
      url='https://github.com/EduScaled/carrier-client',
      author='Nick Lubyanov',
      author_email='lubyanov@gmail.com',
      license='MIT',
      install_requires=['requests', 'jsonschema', 'strict-rfc3339'],
      zip_safe=False)
