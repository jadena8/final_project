import re
from collections import Counter
import numpy as np
import matplotlib.pyplot as plot
import os

bama = "bama_alignment_overlap_fadl.txt"
oprg = "test_oprg.txt"

def reformat_dir(filename):
    with open(filename, "r") as f, open(filename +"_reformated.txt", "w+") as w:
        seq = ""
        begin_line = ""
        count = 0
        seq_counts = []
        for line in f:	
        #num = str(count)
            if ">" in line:
			#write old stuff to single line in file
               
               begin_line = line
               w.write(begin_line)
               w.write(seq + "\n")
               if(len(seq) != 0):
                   seq_counts.append(len(seq))
                   #w.write(seq + "\n")
                   seq = ""			
			#print(begin_line + " " + seq)
			#start over again
			#begin_line = ">sp_" + num
			#print(count)
			#count += 1
            else:
               seq += line.strip()
    return()

#reformat_dir("1A0S_P.fasta")

dir_name = "C:/Users/USER/Documents/Joanna Lab/coevolution/blasted_proteins/psiblasted_prots/130_omp_psiblast_seqs"	
fadl = "fadl_bama_overlap_sp_alignment.txt"

#reformat_dir(bama)
reformat_dir(fadl)
 
#for f in os.listdir(dir_name):
#	reformat_dir(f)
			   
"""			   
			   
#To plot distribution of sequence size

#print(Counter(seq_counts))
seq_counts = (Counter(seq_counts))
print(seq_counts)
labels, values = zip(*Counter(seq_counts).items())

#labels = sorted(labels, key = int)
indexes = np.arange(len(labels))

#indSort = np.argsort(values)[::-1]
#labels = np.array(labels)[indSort]
#values = np.array(values)[indSort] 
#print(indSort)
#print(labels)
#print(values)
indexes = np.arange(len(labels))

width = 1
N = 1000

plot.bar(indexes, values, width)
plot.xticks(indexes + width * 0.5, labels, rotation = 90, fontsize = 8) 
#plot.gca().margins(x=0)
#plot.gcf().canvas.draw()
#tl = plot.gca().get_xticklabels()
#maxsize = max([t.get_window_extent().width for t in tl])
#m = 0.2
#s = maxsize/plot.gcf().dpi*N+2*m
#margin = m/plot.gcf().get_size_inches()[0]

#plot.gcf().subplots_adjust(left=margin, right = 1-margin)
#plot.gcf().set_size_inches(s, plot.gcf().get_size_inches()[1])

plot.xlabel("# of Residues")
plot.ylabel("Frequency")
plot.title("Distribution of AA counts across PSIBlast OprG")
plot.show()
"""