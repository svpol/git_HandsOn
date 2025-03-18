import sys
import re
from argparse import ArgumentParser

def main():
    """
    Classifies a given nucleotide sequence as DNA or RNA, optionally searches for a motif, 
    and calculates nucleotide composition percentages.
    """
    parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
    parser.add_argument("-s", "--seq", type=str, required=True, help="Input nucleotide sequence")
    parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search in the sequence")
    parser.add_argument("-p", "--percentage", action="store_true", help="Enable nucleotide percentage calculation")
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()
    args.seq = args.seq.upper()
    
    classify_sequence(args)

def classify_sequence(args):
    """
    Determines whether the given sequence is DNA or RNA.
    Also performs optional motif search and nucleotide percentage calculation.
    
    Args:
        args (Namespace): Parsed command-line arguments containing sequence, motif, and percentage flag.
    """
    DNA = RNA = False
    
    if re.search(r'^[ACGTU]+$', args.seq):
        if 'T' in args.seq and 'U' not in args.seq:
            print('The sequence is DNA')
            DNA = True
        elif 'U' in args.seq and 'T' not in args.seq:
            print('The sequence is RNA')
            RNA = True
        elif 'T' in args.seq and 'U' in args.seq:
            print('The sequence is not DNA nor RNA')
        else:
            print('The sequence can be DNA or RNA')
            DNA = RNA = True
    else:
        print('The sequence is not DNA nor RNA')
        return
    
    if args.motif:
        search_motif(args.seq, args.motif)
    
    if args.percentage:
        calculate_nucleotide_percentage(args.seq, DNA, RNA)

def search_motif(sequence, motif):
    """
    Searches for a specified motif within the sequence and prints the result.
    
    Args:
        sequence (str): The nucleotide sequence.
        motif (str): The motif to search for in the sequence.
    """
    motif = motif.upper()
    print(f'Motif search enabled: looking for motif "{motif}" in sequence "{sequence}"... ', end='')
    if re.search(motif, sequence):
        print("FOUND")
    else:
        print("NOT FOUND")

def calculate_nucleotide_percentage(sequence, is_dna, is_rna):
    """
    Calculates and prints the nucleotide composition percentages if the sequence is DNA or RNA.
    
    Args:
        sequence (str): The nucleotide sequence.
        is_dna (bool): Flag indicating whether the sequence is classified as DNA.
        is_rna (bool): Flag indicating whether the sequence is classified as RNA.
    """
    if not (is_dna or is_rna):
        print('Percentage calculation is non-applicable.')
        return
    
    nucleotide_counts = {nt: sequence.count(nt) for nt in set(sequence)}
    print('\nNucleotide percentage:')
    for nt, count in nucleotide_counts.items():
        print(f'{nt}\t{round((count / len(sequence)) * 100, 4)}%')

if __name__ == "__main__":
    main()
