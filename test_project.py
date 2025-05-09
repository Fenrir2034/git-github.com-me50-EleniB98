# test_project.py
import pytest
from project import GeneticCode

def test_translate_dna_to_protein():
    # Test case 1: DNA sequence with valid codons
    dna_sequence_1 = "ATGGTGGCCATGTGTCGT"
    expected_protein_sequence_1 = "MVAMCR"

    # Instantiate the GeneticCode class
    genetic_code = GeneticCode()

    # Perform DNA to protein translation
    actual_protein_sequence_1 = genetic_code.dna_to_protein(dna_sequence_1)  # Correct method name

    # Assert the expected protein sequence against the actual output
    assert actual_protein_sequence_1 == expected_protein_sequence_1


def test_reverse_transcribe():
    # Test case: RNA sequence with 'U' replaced by 'T'
    rna_sequence = "AUGUCCGA"
    expected_dna_sequence = "ATGTCCGA"

    # Instantiate the GeneticCode class
    genetic_code = GeneticCode()

    # Perform reverse transcription
    actual_dna_sequence = genetic_code.reverse_transcribe(rna_sequence)

    # Assert the expected DNA sequence against the actual output
    assert actual_dna_sequence == expected_dna_sequence

def test_transcribe_to_rna():
    # Test case: DNA sequence with 'T' replaced by 'U'
    dna_sequence = "ATGTCCGA"
    expected_rna_sequence = "AUGUCCGA"

    # Instantiate the GeneticCode class
    genetic_code = GeneticCode()

    # Perform transcription to RNA
    actual_rna_sequence = genetic_code.transcribe_to_rna(dna_sequence)

    # Assert the expected RNA sequence against the actual output
    assert actual_rna_sequence == expected_rna_sequence
