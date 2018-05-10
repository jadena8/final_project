import re
import os

fadl = "1T16.fasta_reformated.txt"
bama = "reformat_total_bama_blastp_seqs.txt"
def loop_dir(filename):
    species=[]
    i=0
    with open(bama) as inFile:
      for line in inFile:
        line = line.rstrip()
    
        if line.startswith('>'):
          regex = re.compile('(\[(.+?)\].*)')
          try:
            matches = regex.search(line).group(1)[1:-1]
          except AttributeError:
             matches = None		  
        if matches is not None:
          species.append(matches)
 
    unique_sp = list(set(species))

    #print(unique_sp)
    #print(len(unique_sp))
    seq = ""
    count = 0
    resi = []
    with open(filename) as inFile:
        for line in inFile:
            if line.startswith('>'):
                name_line = line
                regex = re.compile('(\[(.+?)\].*)')
                
                try:
                    to_match = regex.search(line).group(1)[1:-1]
                except AttributeError:
                    to_match = None 
			    #print(to_match)
                if to_match is not None:
                    for i in unique_sp:
                        
                        #print(len(seq))
				    #print(i)
                        if i == to_match:
                            #print(name_line, end = "")
                            count += 1
                            seq = next(inFile)
                            #if 780 < len(seq) < 850:
                            print(name_line, end = "")
								#seq = next(inFile)
                                #print(len(seq))
                            resi.append(len(seq))
                            print(seq, end = "")
                        #print(name_line + seq, end = "")
                            unique_sp.remove(i)
                            seq = ""
					
    #print(len(unique_sp))
    #print(len(resi))
    if len(resi) == 0:
        return(count, 0)
    elif len(resi) == 1:
        return(count, resi[0])
    else:
        return(count, resi[1])

dir_name = "C:/Users/USER/Documents/Joanna Lab/coevolution/blasted_proteins/psiblasted_prots/130_omp_psiblast_seqs/reformated_psiblast_seqs"

loop_dir(fadl)

counts = []
#for f in os.listdir(dir_name):
	#counts = str(loop_dir(f))
	#print(f + "\t" + counts)
	
	
	
