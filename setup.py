from setuptools import setup, find_packages

setup(name='carrier',
      version='0.1',
      description='Carrier',
      url='https://github.com/EduScaled/carrier-package',
      author='Nick Lubyanov',
      author_email='lubyanov@gmail.com',
      license='MIT',
      packages=['carrier'],
      install_requires=['requests'],
      zip_safe=False)
