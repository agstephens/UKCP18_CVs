from setuptools import setup, find_packages
from ukcp_cv import __version__


def readme():
    with open('README.md') as f:
        return f.read()


reqs = [line.strip() for line in open('requirements.txt')]


GIT_REPO = "https://github.com/ukcp-data/UKCP18_CVs"

setup(
    name                 = "ukcp-controlled-vocabularies",
    version              = __version__,
    description          = "Python library for reading UKCP controlled vocabularies .",
    long_description     = readme(),
    license              = "",
    author               = "Ag Stephens",
    author_email         = "ag.stephens@stfc.ac.uk",
    url                  = GIT_REPO,
    packages             = find_packages(),
    install_requires     = reqs,
    tests_require        = ['pytest'],
    classifiers          = [
        'Development Status :: 2 - ???',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: ???',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
    include_package_data = True,
    scripts=[],
    entry_points = {},
    package_data = {}
)