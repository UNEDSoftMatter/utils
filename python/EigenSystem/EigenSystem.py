#!/usr/bin/python
# -*- coding: utf-8 -*-

# /*
#  * Filename   : EigenSystem.py
#  *
#  * Created    : 30.09.2022
#  *
#  * Modified   : 
#  *
#  * Author     : jatorre
#  *
#  * Purpose    : Get (and sort) eigenvalues
#  *
#  */

# This program computes the eigensystem (eigenvalues and eigenvector) of a time 
# dependent matrix
# 
#     / A11 A12 A13 \
# A = | A21 A22 A23 |
#     \ A31 A32 A33 /
# 
# This program ensures continuity of the sorted eigenvalues and eigenvectors.
# You may either start from:
#   O1. The unitary eigenvectors (1,0,0), (0,1,0), (0,0,1).
#   O2. A given value for the eigenvectors, provided by an external file.
#   O3. The starting eigenvectors, sorted by python from larger to smaller.

import numpy  as np
import sys    as sys
import common as cr
import aux    as aux

cr.timestamp(sys.argv[1],"Init "+str(sys.argv[0:]))

cr.timestamp(sys.argv[1],"Reading file ")

# Input matrix file should be sorted as:
# STEP A11 A21 A31 A21 A22 A23 A31 A32 A33
SRC  = np.loadtxt(sys.argv[1]+'.dat')

if (len(SRC[0]) != 10):
    sys.exit("ERROR: Input matrix file should be sorted as: \n # STEP A11 A12 A13 A21 A22 A23 A31 A32 A33")

# Parameters
N2     = len(SRC)
step0  = SRC[0,0] 
dstep  = SRC[1,0]-SRC[0,0]

# Compute Eigen
cr.timestamp(sys.argv[1],"Computing eigensystem")

fEIGEN    = open(sys.argv[1]+'_eval.dat', 'w')
fROTATION = open(sys.argv[1]+'_evec.dat', 'w')

e0old = np.zeros((3,3))
M     = np.zeros(3)

# O1.
cr.timestamp(sys.argv[1],"Initial sorting by e_x,e_y,e_z")
FirstSorting = 0
e0old[:,0]   = [1.0,0.0,0.0] 
e0old[:,1]   = [0.0,1.0,0.0] 
e0old[:,2]   = [0.0,0.0,1.0] 

# O2.
# cr.timestamp(sys.argv[1],"Initial sorting by previous file")
# FirstSorting = 0
# e0original   = np.loadtxt('./'+sys.argv[1]+'_rotation_original.dat')
# Moriginal    = np.loadtxt('./'+sys.argv[1]+'_M_original.dat')
# e0old[:,0]   = e0original[1:4]
# e0old[:,1]   = e0original[4:7]
# e0old[:,2]   = e0original[7:10]
# M[0]         = Moriginal[1]
# M[1]         = Moriginal[2]
# M[2]         = Moriginal[3]
# del e0original
# del Moriginal

# O3
# cr.timestamp(sys.argv[1],"Initial sorting from largest to smallest")
# FirstSorting=1

step  = step0

for i in range (0,N2):

  Ji = np.reshape(SRC[i,1:10],(3,3))
  
  # Diagonalize and sort J
  M,e0     = np.linalg.eig(Ji)
  if (FirstSorting==0):
    M,e0  = aux.SortEigen(e0old,e0,M)
  else:
    idx = M.argsort()[::-1]    # Largest to smallest
    # idx = M.argsort()        # Smallest to largest
    M   = M[idx]
    e0  = e0[:,idx]
    FirstSorting = 0
  e0old = e0
     
  # Save eigenvalues
  out      = np.append(step, M)
  out      = np.array([out])
  np.savetxt(fEIGEN, out, fmt='%20.12E')
  
  # Save eigenvectors
  R           = np.transpose(e0)
  out         = np.append(step, R)
  out         = np.array([out])
  np.savetxt(fROTATION, out, fmt='%20.12E')

  step += dstep

fROTATION.close()
fEIGEN.close()
del SRC

cr.timestamp(sys.argv[1],"EOF "+sys.argv[0])
