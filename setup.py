"""\
Provides a python package to get data of academic papers abstracts
posted at arXiv.org in a specific date range and category.
"""

import sys
try:
    from setuptools import setup, find_packages
except ImportError:
    sys.exit("""Error: Setuptools is required for installation.
 -> http://pypi.python.org/pypi/setuptools""")

setup(
    name = "arxivabsscraper",
    version = "0.1",
    description = "Get arXiv.org abstracts within a date range and category",
    author = "Mohamed Elashri",
    author_email = "muhammadelashri@gmail.com",
    url = "https://github.com/MohamedElashri/Arxiv-Aabstract-scraper",
    download_url = 'https://github.com/MohamedElashri/Arxiv-Aabstract-scraper/archive/0.1.tar.gz',
    py_modules = [""],
    packages=find_packages(),
    keywords = ["arxiv", "scraper", "api", "citation"],
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Markup :: LaTeX",
        ],
)
