import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def pair(i,j):
    if ((i=='A') & (j=='U'))|((i=='U') & (j=='A')):
        return 2
    elif ((i=='G') & (j=='C'))|((i=='C') & (j=='G')):
        return 3
    elif ((i=='G') & (j=='U'))|((i=='U') & (j=='G')):
        return 1
    else:
        return 0


def Fill(DP, i, j):
    structure = []
    
    structure.append(DP[i+1][i+j])
    structure.append(DP[i][i+j-1])
    structure.append(DP[i+1][i+j-1]+pair(sequence[i],sequence[i+j]))
    
    if i+3<=i+j:
        tmp=[]
        for k in range(i+1,j+i):
            tmp.append(DP[i,k]+DP[k+1,i+j]);
        structure.append(max(tmp))

    return max(structure)


def traceback(i,j,pair1):
  if i<j:
    if DP[i,j]==DP[i+1,j]:
      traceback(i+1,j,pair1)
    elif DP[i,j]==DP[i,j-1]:
      traceback(i,j-1,pair1)
    elif DP[i,j]==(DP[i+1,j-1]+pair(sequence[i],sequence[j])):
      pair1.append([i,j,str(sequence[i]),str(sequence[j])])
      traceback(i+1,j-1,pair1);
    else:
      for k in range(i+1,j):
        if DP[i,j]==DP[i,k]+DP[k+1,j]:
          traceback(i,k,pair1);
          traceback(k+1,j,pair1);
          break;
  return pair1;

def write_structure(structure):
    dot_bracket = ["." for _ in range(len(sequence))]
    print structure
    for s in structure:
        dot_bracket[min(s)] = "("
        dot_bracket[max(s)] = ")"
    return "".join(dot_bracket)


sequence = "ACCACGCUUAAGACACCUAGCUUGUGUCCUGGAGGUCUAGCCGUCAGACCGCGAGAGGGACACUCGAUUUAGGCG"


N = len(sequence)
structure = []

DP = np.zeros((N,N))
count=0
for j in range(1,N):
    for i in range(0,N-j):

        DP[i][i+j]=Fill(DP,i,j)


print DP
struct=[]
pair1=traceback(0,N-1,[])
print "max # of folding pairs: ",len(pair1);
for x in range(0,len(pair1)):
    
    pair1[x][1]=pair1[x][1]-pair1[x][0]-1
    if (pair1[x][1]>=3) :
        print '%d %d %s==%s' % (pair1[x][0],pair1[x][1]+pair1[x][0]+1,pair1[x][2],pair1[x][3]);
        struct.append((pair1[x][0],pair1[x][1]+pair1[x][0]+1))


dot_brac_notation = write_structure(struct)
print dot_brac_notation
