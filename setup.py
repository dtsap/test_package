from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='test_package',
      version='0.2',
      description='This is a testing package',
      url='',
      author='Mits Tsap',
      author_email='mitstsap@example.com',
      license='MIT',
      packages=['test_package'],
      zip_safe=False,
      python_requires='>=3')
