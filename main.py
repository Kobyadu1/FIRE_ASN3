import pandas as pd
from Bio import Entrez
from Bio import Entrez, SeqIO

Entrez.email = "kobyadu1@gmail.com"

def _n_count(s):
    return s.count('N')

n_count = []
data = pd.read_csv('koby.csv')

for s in data['Accession']:
    handle = Entrez.efetch(db="nucleotide", id=Entrez.read(Entrez.esearch(db="nucleotide", term=s))['IdList'][0],
                           rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    n_count.append(_n_count(record.seq))

data['n_count'] = n_count
data.to_csv('koby_new',index=False)
