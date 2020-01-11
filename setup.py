# from setuptools import setup
from distutils.core import setup

files = ["resource/*"]

setup(name = "supermarket",
    version = "0.3",
    description = "Supermarket Shopping cart Checkout system",
    author = "Sanjeev Kumar",
    author_email = "sanjeev@outlook.in",
    packages = ['supermarket'],
    include_package_data=True,
    package_data = {'package' : ["resource/*"]},
    scripts = ["scripts/supermarket"],
    long_description = """A simple Supermarket Shopping cart Checkout system.""",
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: Unix',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development',
            ],
       platforms=['Unix', 'Darwin', 'Windows']

) 