from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='shopify-scraper',
      version='0.1',
      description='Shopify Reviews Scraper',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='danielfvalverde@gmail.com',
      license='MIT',
      packages=['shopify_scraper'],
      install_requires=[
      	"mechanize",
      	"lxml",
      ],
      zip_safe=False)
