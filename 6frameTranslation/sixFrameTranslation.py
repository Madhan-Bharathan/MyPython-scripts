# Name: Madhan
# Assignment: Task 1 (Six frame DNA translation)
# Date: 19 November 2021




# Function for printing the protein equivalent of codons
def dnaToProtein(dnaSeq):
      
  table = {
      'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
      'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
      'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
      'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',    
      'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
      'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
      'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
      'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
      'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
      'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
      'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
      'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
      'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
      'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
      'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
      'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
  }
  protein =""
  # if len(dnaSeq)%3 == 0:
  for i in range(0, len(dnaSeq), 3):
    codon = dnaSeq[i:i + 3]
    if len(codon)==3:
      protein+= table[codon]
    else:
      return protein
  return protein

# Function for translating proteins
def Translation(protein):

  proteinTable = {
      'I':'lle','M':'Met','T':'Thr',
      'N':'Asn','K':'Lys','S':'Ser',  
      'R':'Arg','L':'Leu','P':'Pro', 
      'H':'His','Q':'Gln','V':'Val',
      'A':'Ala','D':'Asp','E':'Glu', 
      'G':'Gly','F':'Phe','Y':'Tyr', 
      '*':'Ter','C':'Cys','W':'Trp',
  }
  trans=""
  
  for i in range(0, len(protein)):
    codon = protein[i]
    trans+= proteinTable[codon]
  return trans


# Code for reading and deleting the first line
# with open('sequence.txt', 'r') as fin:
#     data = fin.read().splitlines(True)
# with open('input.txt', 'w') as fout:
#     fout.writelines(data[1:])

# Opening and reading the file which contains the original DNA sequence
inputfile ="input.txt"
f = open(inputfile, "r")
dnaSeq = f.read()

# # Removing the newline characters
# dnaSeq=dnaSeq.replace('\n',"")
# f = open(inputfile, "w")
# # Writting into the same file 
# f.writelines(dnaSeq) 
# dnaSeq=dnaSeq.replace(dnaSeq[-1],"")


print("Forward : ")
print("")
# Loop to view in all read all frames
for i in range(0,3,1):
  print("> - {}  Nucleotides : ".format(len(dnaSeq[i:])))
  currentFDna=dnaSeq[i:]
  # Loop to print the DNA sequence in pairs of 3 in console
  for k in range(0,len(currentFDna),3):
    print(currentFDna[k:k+3],end=" ")
  print(" ")
  print("Protein : ")
  # Calling the function to find the protein equivalent of DNA sequence
  protein=dnaToProtein(dnaSeq[i:])
  print(protein)
  print("> - {}  Codons : ".format(len(protein)))
  # Calling the Translation function
  print(Translation(protein))
  print(" ")


print("Reverse")
print("")
# Reversing the original DNA sequence
revDnaSeq=dnaSeq[::-1]
# Loop to view in all read all frames
for i in range(0,3,1):
  print("> - {}  Reverse Nucleotides : ".format(len(revDnaSeq[i:])))
  currentRDna=revDnaSeq[i:]
  for k in range(0,len(currentRDna),3):
    print(currentRDna[k:k+3],end=" ")
  print(" ")
  print("Protein : ")
  protein=dnaToProtein(revDnaSeq[i:])
  print(protein)
  print("> - {}  Codons : ".format(len(protein)))
  # Calling the Translation function
  print(Translation(protein))

