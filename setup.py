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
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name = "arxivabscraper",
    version = "0.1",
    description = "Get arXiv.org abstracts within a date range and category",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = "Mohamed Elashri",
    author_email = "muhammadelashri@gmail.com",
    url = "https://github.com/MohamedElashri/Arxiv-Aabstract-scraper",
    download_url = 'https://github.com/MohamedElashri/Arxiv-Aabstract-scraper/archive/0.2.tar.gz',
    py_modules = [""],
    packages=find_packages(),
    keywords = ["arxiv", "scraper", "api", "citation"],
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Markup :: LaTeX",
        ],
)
