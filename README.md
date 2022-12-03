# biomapy

his is a library that has just one function that maps a list of gene IDs from one to another. Supported IDs are Uniprot, entrez, ensembl, a    nd symbol. The usage is straightforward the gene_mapping_many() takes as argument the list of IDs, source IDs and target IDs. It is a little slow when imported be    cause every time reads the file on ncbi and UniProt so that remains updated. Future implementations will fous on download the data just once and feed the path to     the library and to expand the IDs that are supported
