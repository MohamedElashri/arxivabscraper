[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4395835.svg)](https://doi.org/10.5281/zenodo.4395835)

# arxivabscraper
An ArXiV scraper to retrieve abstracts from given categories and date range. [website](https://mohamedelashri.github.io/arxivabscraper/)

## Install

Use `pip` (or `pip3` for python3):

```bash
$ pip install arxivabscraper
```

or download the source and use `setup.py`:

```bash
$ python setup.py install
```

or if you do not want to install the module, copy `arxivabscraper.py` into your working
directory.

To update the module using `pip`:
```bash
pip install arxivabscraper --upgrade
```

## Examples

There is a tutorial on how to use the package directly on google colab [here](https://github.com/MohamedElashri/Arxiv-Aabstract-scraper/blob/main/arxivabscraper_tutorial.ipynb)
 . 
it provides the basic usage to the package and can be run directly on the notebook

You can directly use `arxivabscraper` in your scripts. Let's import `arxivabscraper`
and create a scraper to fetch all preprints in condensed matter physics category
from 2 May 2018 until 2 June 2020 (for other categories, see below):

```python
import arxivabscraper
scraper = arxivabscraper.Scraper(category='physics:hep-th', date_from='2010-05-27',date_until='2020-06-07')
```
Once we built an instance of the scraper, we can start the scraping:

```python
output = scraper.scrape()
```
While scraper is running, it prints its status:

```
fetching up to  1000 records...
fetching up to  2000 records...
Got 503. Retrying after 30 seconds.
fetching up to  3000 records...
fetching is complete.
```

Finally you can save the output in your favorite format or readily convert it into a pandas dataframe:
```python
import pandas as pd
cols = ('categories', 'abstract')
df = pd.DataFrame(output,columns=cols)
```


## Categories
Here is a list of all categories available on ArXiv.

| Category | Code |
| --- | --- |
| Computer Science | `cs` |
| Economics | `econ` |
| Electrical Engineering and Systems Science | `eess` |
| Mathematics | `math` |
| Physics | `physics` |
| Astrophysics | `physics:astro-ph` |
| Condensed Matter | `physics:cond-mat` |
| General Relativity and Quantum Cosmology | `physics:gr-qc` |
| High Energy Physics - Experiment | `physics:hep-ex` |
| High Energy Physics - Lattice | `physics:hep-lat` |
| High Energy Physics - Phenomenology | `physics:hep-ph` |
| High Energy Physics - Theory | `physics:hep-th` |
| Mathematical Physics | `physics:math-ph` |
| Nonlinear Sciences | `physics:nlin` |
| Nuclear Experiment | `physics:nucl-ex` |
| Nuclear Theory | `physics:nucl-th` |
| Physics (Other) | `physics:physics` |
| Quantum Physics | `physics:quant-ph` |
| Quantitative Biology | `q-bio` |
| Quantitative Finance | `q-fin` |
| Statistics | `stat` |

## Contributing
Ideas/bugs/comments? Please open an issue or submit a pull request on Github.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
This work is based on the arxivscraper from 
Mahdi Sadjadi (2017). arxivscraper: Zenodo. http://doi.org/10.5281/zenodo.889853
