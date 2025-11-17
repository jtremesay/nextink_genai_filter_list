# Next.ink GenAI filter list

Try to rebuild the list of sites in the [Extension-Alerte-GenAI](https://github.com/Gathor59/Extension-Alerte-GenAI) extension for Firefox and Chrome.

Latest published version of the filter can be found in the `domains_in_filter_<date>.txt` file.


## Usage

Fetch latest version of the filter:

```shell
$ python dl_last_filter.py
```

Extract the list of domains from the filter:

```shell
$ python gen_list.py
```


## Data sources:

- .fr domains: https://www.afnic.fr/produits-services/services-associes/donnees-partagees/