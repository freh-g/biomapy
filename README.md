# biomapy

This is a library that has just one function that maps a list of gene IDs from one to another. 

Supported IDs are Uniprot, entrez, ensembl, and Gene_symbol. 

The usage is straightforward the gene_mapping_many() takes as argument the list of IDs As a Python object list), source ID type  and target ID type. 

The funciton update_mapping_datasets() serves to update the mapping datasets and to be sure that your mappings are up-to-date.

Be careful that the data type is compatible when you map. Entrez have to be ints and not strings.

Future implementations will fous on expanding the IDs that are supported (e.g. diseases)

## Installation

Biomapy can be installed via pip

```
pip install biomapy

```

## Usage

A tipical call for gene_mapping_many() is as follows:

```
gene_symbol_list=['A1BG','TGFB','BMP2']

gene_entrez_list=gene_mapping_many(gene_symbol_lyst,'symbol','entrez')

gene_entrez_list

```

**Output:**

[1,7040,650]
