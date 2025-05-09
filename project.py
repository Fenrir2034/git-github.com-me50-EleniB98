# project.py

class GeneticCode:
    def __init__(self):
        # Initialize the GeneticCode class with a codon table
        self.codon_table = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
            'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
        }

    def dna_to_protein(self, dna_sequence):
        """
        Translates a DNA sequence to a protein sequence using the genetic code.

        :param dna_sequence: The input DNA sequence
        :return: The resulting protein sequence
        """
        protein_sequence = ""
        for i in range(0, len(dna_sequence), 3):
            codon = dna_sequence[i:i + 3]
            if codon in self.codon_table:
                protein_sequence += self.codon_table[codon]
            else:
                protein_sequence += "-"

        return protein_sequence.rstrip("-")

    def reverse_transcribe(self, rna_sequence):
        """
        Reverse transcribes an RNA sequence to a DNA sequence.

        :param rna_sequence: The input RNA sequence
        :return: The resulting DNA sequence
        """
        return rna_sequence.replace('U', 'T')

    def transcribe_to_rna(self, dna_sequence):
        """
        Transcribes a DNA sequence to an RNA sequence.

        :param dna_sequence: The input DNA sequence
        :return: The resulting RNA sequence
        """
        return dna_sequence.replace('T', 'U')


def main():
    # Instantiate the GeneticCode class
    genetic_code = GeneticCode()

    # Prompt the user to choose the operation
    user_input = input(
        "Enter 'D' for DNA to protein conversion, 'R' for reverse transcription, 'T' for transcription to RNA: "
    ).upper()

    if user_input == 'D':
        # DNA to protein conversion
        dna_sequence = input("Enter the DNA sequence: ").upper()
        protein_sequence = genetic_code.dna_to_protein(dna_sequence)  # Correct method name
        print("Protein sequence:", protein_sequence)

    elif user_input == 'R':
        # Reverse transcription from RNA to DNA
        rna_sequence = input("Enter the RNA sequence: ").upper()
        dna_sequence = genetic_code.reverse_transcribe(rna_sequence)
        print("Reverse Transcribed DNA sequence:", dna_sequence)

    elif user_input == 'T':
        # Transcription from DNA to RNA
        dna_sequence = input("Enter the DNA sequence: ").upper()
        rna_sequence = genetic_code.transcribe_to_rna(dna_sequence)
        print("Transcribed RNA sequence:", rna_sequence)

    else:
        # Handle invalid input
        print("Invalid input. Please enter 'D', 'R', or 'T'.")

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()



