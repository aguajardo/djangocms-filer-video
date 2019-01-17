import os

from setuptools import setup, find_packages

djangocms_filer_video = __import__('djangocms_filer_video')


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')
CHANGES = read('CHANGES.rst')

setup(
    name='djangocms-filer-video',
    packages=find_packages(),
    version=djangocms_filer_video.get_version(),
    author='Mark Trifonov',
    author_email='air.t.mark@gmail.com',
    url='https://github.com/Air-Mark/djangocms-filer-video',
    description=djangocms_filer_video.__doc__.strip(),
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords=['django', 'djangocms' 'filer', 'video'],
    install_requires=[
        'Django >=1.8, <=1.11',
    ],
    test_suite='nose.collector',
)
