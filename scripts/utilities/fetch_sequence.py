"""Fetch sequences from NCBI using accession numbers."""
from Bio import Entrez, SeqIO


def fetch_sequence(accession: str, email: str, database: str = "nucleotide") -> str:
    Entrez.email = email
    handle = Entrez.efetch(db=database, id=accession, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return record


if __name__ == "__main__":
    record = fetch_sequence("NM_001301717", "your.email@example.com")
    print(f"ID: {record.id}")
    print(f"Length: {len(record.seq)}")
    print(f"Description: {record.description}")
