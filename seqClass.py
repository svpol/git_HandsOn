import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
parser.add_argument("-p", "--percentage", action="store_true", help="Enable nucleotide percentage calculation")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 


DNA = False
RNA = False


if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq):
        print ('The sequence is DNA')
        DNA = True
    elif re.search('U', args.seq) and not re.search('T', args.seq):
        print ('The sequence is RNA')
        RNA = True
    elif re.search('T', args.seq) and re.search('U', args.seq):
        print('The sequence is not DNA nor RNA')
    else:
        print ('The sequence can be DNA or RNA')
        DNA = True
        RNA = True
else:
    print ('The sequence is not DNA nor RNA')
    
# Motif search
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
        
# Percentage calculation
if args.percentage:
    nucleotides = {}
    for letter in set(args.seq):
        nucleotides[letter] = 0
    if DNA == True or RNA == True:
        for i in args.seq:
    	    for k in nucleotides.keys():
    	        if i == k:
    	            nucleotides[k] += 1
        print(f'\nNucleotide percentage:')  
        for key in nucleotides:
            print(f'{key}\t{round(nucleotides[key]/len(args.seq), 4)*100}')
    else:
        print('Percentage calculation is non-applicable.')
        
        
        
        
