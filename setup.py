from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path


setup(
    name='biomapy',
    packages=find_packages(),
    include_package_data=True,
    package_data={'biomapy': ['datasets/*.gz']},
    version='0.2.2',
    install_requires=['wget'],
    long_description='This is a library that has just one function that maps a list of gene IDs from one to another. Supported IDs are Uniprot, entrez, ensembl, and symbol. The usage is straightforward the gene_mapping_many() takes as argument the list of IDs, source IDs and target IDs. The function update_datasets() will update the map datasets directly from uniprot and ncbidb. Future implementations will focus on expanding the possibility of mapping between IDs.',
    author='Francesco Gualdi',
    license='MIT'
)
