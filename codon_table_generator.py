"""
Codon Table Generator
A beginner-friendly Python program to translate DNA or RNA sequences.
"""

# Standard genetic code: all 64 DNA codons
CODON_TABLE = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine", "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine", "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine", "ATA": "Isoleucine",
    "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine", "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine",
}

START_CODONS = {"ATG"}
STOP_CODONS = {"TAA", "TAG", "TGA"}
VALID_DNA = set("ATGC")
VALID_RNA = set("AUGC")


def display_codon_table():
    """Print all codons and their amino-acid meanings."""
    print("\nSTANDARD DNA CODON TABLE")
    print("-" * 35)
    for codon in sorted(CODON_TABLE):
        notes = ""
        if codon in START_CODONS:
            notes = " (Start)"
        elif codon in STOP_CODONS:
            notes = " (Stop)"
        print(f"{codon} -> {CODON_TABLE[codon]}{notes}")
    print(f"\nTotal codons: {len(CODON_TABLE)}")


def validate_sequence(sequence, sequence_type):
    """Check whether a sequence contains only valid DNA or RNA letters."""
    allowed = VALID_DNA if sequence_type == "DNA" else VALID_RNA
    invalid_letters = sorted(set(sequence) - allowed)
    if invalid_letters:
        letters = ", ".join(invalid_letters)
        print(f"Invalid input: {letters}")
        print(f"{sequence_type} sequences may contain only {''.join(sorted(allowed))}.")
        return False
    if not sequence:
        print("The sequence cannot be empty.")
        return False
    return True


def translate_sequence(sequence, sequence_type):
    """Split a sequence into codons and translate complete codons."""
    # Convert RNA U to DNA T so the same standard table can be used.
    dna_sequence = sequence.replace("U", "T") if sequence_type == "RNA" else sequence

    complete_length = len(dna_sequence) - (len(dna_sequence) % 3)
    complete_sequence = dna_sequence[:complete_length]
    leftover = dna_sequence[complete_length:]

    codons = [complete_sequence[i:i + 3] for i in range(0, len(complete_sequence), 3)]

    print("\nTRANSLATION RESULTS")
    print("-" * 50)
    print(f"{'Codon':<10}{'Amino acid / meaning':<25}{'Note'}")
    print("-" * 50)

    amino_acids = []
    for codon in codons:
        amino_acid = CODON_TABLE[codon]
        note = ""
        if codon in START_CODONS:
            note = "Start codon"
        elif codon in STOP_CODONS:
            note = "Stop codon"
        print(f"{codon:<10}{amino_acid:<25}{note}")
        amino_acids.append(amino_acid)

    print("\nCodons:", " - ".join(codons) if codons else "No complete codons")
    print("Amino acids:", " - ".join(amino_acids) if amino_acids else "None")

    start_positions = [i + 1 for i, codon in enumerate(codons) if codon in START_CODONS]
    stop_positions = [i + 1 for i, codon in enumerate(codons) if codon in STOP_CODONS]
    print("Start codon position(s):", start_positions if start_positions else "None found")
    print("Stop codon position(s):", stop_positions if stop_positions else "None found")

    if leftover:
        print(f"Warning: incomplete codon at the end: {leftover} (ignored during translation)")
    else:
        print("Incomplete codon at the end: None")


def main():
    print("CODON TABLE GENERATOR")
    print("Translate a DNA or RNA sequence into amino acids.")

    while True:
        sequence_type = input("\nEnter sequence type (DNA/RNA): ").strip().upper()
        if sequence_type in {"DNA", "RNA"}:
            break
        print("Please enter DNA or RNA.")

    sequence = input(f"Enter your {sequence_type} sequence: ").strip().upper()
    if not validate_sequence(sequence, sequence_type):
        print("Please run the program again and enter a valid sequence.")
        return

    display_codon_table()
    translate_sequence(sequence, sequence_type)


if __name__ == "__main__":
    main()
