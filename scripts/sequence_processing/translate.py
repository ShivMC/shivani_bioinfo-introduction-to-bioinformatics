"""Translate DNA sequences to protein."""
from Bio.Seq import Seq


def translate_dna(dna: str, table: int = 1) -> str:
    seq = Seq(dna)
    return str(seq.translate(table=table))


def gc_content(dna: str) -> float:
    seq = Seq(dna)
    from Bio.SeqUtils import GC
    return GC(seq)


if __name__ == "__main__":
    dna = "ATGCGTACGATCGATCGATCGATCGTAGCTAGCTAGCTAGCTAGC"
    print(f"DNA: {dna}")
    print(f"Protein: {translate_dna(dna)}")
    print(f"GC Content: {gc_content(dna):.2f}%")
