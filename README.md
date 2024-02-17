# q2-surpi

q2-surpi is a plugin supporting the import of SURPI results for use in QIIME 2.

## Installation

q2-surpi requires an existing QIIME 2 environment (see documentation at
https://docs.qiime2.org for QIIME 2 installation instructions).  To install 
the plugin, first activate the QIIME 2 environment and then install the 
plugin repository from github:

```
pip install git+https://github.com/AmandaBirmingham/q2-surpi.git
```

After this, it is necessary to refresh the QIIME 2 plugin cache:

```
qiime dev refresh-cache
```

The q2-surpi plugin should now be in the list of installed plugins produced
by running `qiime --help`