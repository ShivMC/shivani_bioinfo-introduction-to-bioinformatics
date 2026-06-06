"""Basic BLAST search example using Biopython."""
from Bio.Blast import NCBIWWW, NCBIXML


def run_blast(sequence: str, program: str = "blastn", database: str = "nt") -> list:
    result_handle = NCBIWWW.qblast(program, database, sequence)
    blast_records = NCBIXML.parse(result_handle)
    results = []
    for record in blast_records:
        for alignment in record.alignments[:5]:
            for hsp in alignment.hsps[:1]:
                results.append({
                    "title": alignment.title,
                    "length": alignment.length,
                    "e_value": hsp.expect,
                    "score": hsp.score,
                    "identities": f"{hsp.identities}/{hsp.align_length}",
                })
    return results


if __name__ == "__main__":
    seq = "ATGCGTACGATCGATCGATCGATCGTAGCTAGCTAGCTAGCTAGC"
    hits = run_blast(seq)
    for hit in hits:
        print(f"{hit['title']} | E={hit['e_value']} | {hit['identities']}")
