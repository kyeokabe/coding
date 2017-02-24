#A: mxn (2x4) note:m=len(A), n=len(A[0])
#B: nxp (4x3) note:p=len(B[0])
#C: mxp (2x3)

###Answer Function###
def matmul(A,B):
  C=[]
  D=[]
  for m in range(0,len(A)):
    for p in range(0,len(B[0])):
      #defined index here because using C[m][p] doesn't work like numpy
      #(cannot write into individual indices correctly this way)
      index=0
      for n in range(0,len(A[0])):
        index+=A[m][n]*B[n][p]
      C.append(index)
  #reshape "C" into 2D matrix "D"
  for x in range(0,len(A)):
    D.append(C[x*len(B[0]):(x+1)*len(B[0])])
  return D

"""
###test section###
A=[[4, 2, 1,6],[6, 8, 3,0]]
B=[[3 ,2, 5],[0,1, 2],[2,2, 1],[0,1,3]]

print matmul(A,B)

#test with numpy
import numpy as np
Q=np.array([[4, 2, 1,6],[6, 8, 3,0]])
R=np.array([[3 ,2, 5],[0,1, 2],[2,2, 1],[0,1,3]])

print np.dot(Q,R)

"""
