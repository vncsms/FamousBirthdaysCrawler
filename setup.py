from setuptools import setup

setup(name='famous',
      version='0.1',
      description='Famous birthday crawler',
      url='https://github.com/vncsms/FamousBirthdaysCrawler',
      author='Vinicius Morais',
      author_email='vmsabc@gmail.com',
      license='MIT',
      python_requires='>=3',
      install_requires=['beautifulsoup4', 'requests'],
      packages=['famous'],
      zip_safe=False)