from setuptools import setup

import unittest
def test_suite():
	test_loader = unittest.TestLoader()
	test_suite = test_loader.discover('tests', pattern='test_*.py')
	return test_suite

setup(
    name='ppb-vector',
    version='0.2',
    packages=['ppb_vector'],
    url='http://github.com/pathunstrom/ppb-vector',
    license='',
    author='Piper Thunstrom',
    author_email='pathunstrom@gmail.com',
    description='A basic game development Vector2 class.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
	test_suite='setup.test_suite'
)
