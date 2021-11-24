# Assignment Name : DNA sequence to Protein equivalent
# Date       : 15 Nov 2021
# Time Taken :  8 Hours
# Reference1 : https://www.geeksforgeeks.org
# Reference2 : https://stackoverflow.com/ 
# Reference3 : https://www.genscript.com/tools/codon-table 
# Author name : B Madhan
# Take away  : In depth understanding of Tkinter module and learnt how to implement the tanslation of DNA sequence to amino acids and color them with different colors in a GUI


# Importing the required modules
from tkinter import *  
import random
import string

# Configuring the Tkinter window
top = Tk(className=' Translating DNA to Protein')  
text = Text(top)
text.configure(bg='gray79')
text.pack()

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
  if len(dnaSeq)%3 == 0:
    for i in range(0, len(dnaSeq), 3):
      codon = dnaSeq[i:i + 3]
      protein+= table[codon]
  return protein

# Function for highlighting the proteins with diff colors
def highlight(backg,j,lineno):
  n=3
  tagname = ''.join(random.choices(string.ascii_uppercase+string.digits, k = n))
  text.tag_add(tagname, f"{lineno}.{j}")
  text.tag_config(tagname, background=backg,font='bold')

# Function for finding color for each protein
def color(protein,lineno):
  colorcode={'A':"green yellow",'R':"blue", 'N':"magenta3",'D':"red",'C':"yellow",'E':"deeppink2",'Q':"violetred",'G':"dark orange",'H':"royal blue",'I':"green2",'L':"green2",'K':"SlateBlue4",'M':"lime green",'F':"green3",'P':"goldenrod1",'S':"OrangeRed2",'T':"chocolate2",'W':"deep sky blue",'Y':"cyan",'V':"chartreuse2",'*':"wheat1"}
  j=0
  for i in range(0,len(protein)):
    temp=protein[i]
    backg=colorcode[temp]
    highlight(backg,j,lineno)
    j+=1

# Function for inserting DNA sequence in GUI
def dnaInserting(insertstring,info):
  
  text.insert(INSERT,info+"\n")
  # Loop for inserting the DNA sequence in pairs of 3 in GUI
  for count in range(0,len(insertstring),3):
    text.insert(INSERT, insertstring[count:count+3]+" ")
  text.insert(INSERT,"\n")

# Function for inserting protein sequence in GUI
def proteinInserting(insertstring,info,lineno):
  
  text.insert(INSERT,info+"\n")
  text.insert(INSERT, insertstring+"\n")
  color(insertstring,lineno)

# Main function
def main():

  # Opening and reading the file which contains the original DNA sequence
  inputfile ="original.txt"
  f = open(inputfile, "r")
  dnaSeq = f.read()
  # Converting the DNA sequence to upper case
  dnaSeq=dnaSeq.upper()
  # Declaring and initialising line number for coloring the proteins
  lineno=4


  print("Forward : ")
  print("")
  # Loop to view in all read all frames
  for i in range(0,6,3):
    print("DNA Seq : ")
    currentFDna=dnaSeq[i:]
    info="DNA Seq : "
    # Calling to function to insert the DNA sequence in GUI
    dnaInserting(currentFDna,info)
    # Loop to print the DNA sequence in pairs of 3 in console
    for k in range(0,len(currentFDna),3):
      print(currentFDna[k:k+3],end=" ")
    print(" ")
    print("Protein : ")
    # Calling the function to find the protein equivalent of DNA sequence
    protein=dnaToProtein(dnaSeq[i:])
    print(protein)
    info="Protein : "
    # Calling to function to insert the protein in GUI
    proteinInserting(protein,info,lineno)
    # Incrementing the line number which denotes the line to be colored
    lineno+=4
    print("")
  

  print("Reverse")
  print("")
  # Reversing the original DNA sequence
  revDnaSeq=dnaSeq[::-1]
  # Loop to view in all read all frames
  for i in range(0,6,3):
      print("DNA Seq : ")
      currentRDna=revDnaSeq[i:]
      info="Reverse DNA Seq : "
      # Calling to function to insert the reverse DNA sequence in GUI
      dnaInserting(currentRDna,info)
      # Loop to print the reverse DNA sequence in pairs of 3 in console
      for k in range(0,len(currentRDna),3):
        print(currentRDna[k:k+3],end=" ")
      print(" ")
      print("Protein : ")
      # Calling the function to find the protein equivalent of reverse DNA sequence
      protein=dnaToProtein(revDnaSeq[i:])
      print(protein)
      info="Reverse protein : "
      # Calling to function to insert the reverse protein in GUI
      proteinInserting(protein,info,lineno)
      # Incrementing the line number which denotes the line to be colored
      lineno+=4
      print("")

main()


