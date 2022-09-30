#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import numpy as np

# SortEigen(e0old,e0,M)
#  e0old: previous computed eigenvectors
#  e0:    new (sorted) eigenvectors
#  M:     new (sorted) eigenvalues
#
#  This function sorts the eigenvectors e0 so that
#  to be the closest ones to e0old. It computes the
#  distance between vectors and rearrange them to
#  match the previous ones. Eigenvalues M are sorted
#  accordingly to match their eigenvectors e0.

def SortEigen(A,B,M):
  # Sort First 
  l0  =  A[:,0] 
  o1p =  B[:,0]
  o1m = -B[:,0]
  o2p =  B[:,1]
  o2m = -B[:,1]
  o3p =  B[:,2]
  o3m = -B[:,2]

  l00 = np.dot(o1p-l0,o1p-l0)
  l01 = np.dot(o2p-l0,o2p-l0)
  l02 = np.dot(o3p-l0,o3p-l0)
  l03 = np.dot(o1m-l0,o1m-l0)
  l04 = np.dot(o2m-l0,o2m-l0)
  l05 = np.dot(o3m-l0,o3m-l0)
 
  l   = np.array([l00,l01,l02,l03,l04,l05])
  idx = min(range(len(l)), key=l.__getitem__)

  # print idx, l
  if (idx == 1):
    B[:,[0,1]] = B[:,[1,0]]
    M[[0,1]] = M[[1,0]]
  elif (idx == 2):
    B[:,[0, 2]] = B[:, [2, 0]]
    M[[0,2]] = M[[2,0]]
  elif (idx == 3):
    B[:,0] *= -1.0
  elif (idx == 4):
    B[:,[0, 1]] = B[:, [1, 0]]
    M[[0,1]] = M[[1,0]]
    B[:,0] *= -1.0
  elif (idx == 5):
    B[:,[0, 2]] = B[:, [2, 0]]
    M[[0,2]] = M[[2,0]]
    B[:,0] *= -1.0

  # Sort Second 
  l0  =  A[:,1]
  o2p =  B[:,1]
  o2m = -B[:,1]
  o3p =  B[:,2]
  o3m = -B[:,2]

  l02 = np.dot(o2p-l0,o2p-l0)
  l03 = np.dot(o3p-l0,o3p-l0)
  l04 = np.dot(o2m-l0,o2m-l0)
  l05 = np.dot(o3m-l0,o3m-l0)
 
  l   = np.array([l02,l03,l04,l05])
  idx = min(range(len(l)), key=l.__getitem__)

  # print idx, l
  if (idx == 1):
    B[:,[1, 2]] = B[:, [2, 1]]
    M[[1,2]] = M[[2,1]]
  elif (idx == 2):
    B[:,1] *= -1.0
  elif (idx == 3):
    B[:,[1, 2]] = B[:, [2, 1]]
    M[[1,2]] = M[[2,1]]
    B[:,1] *= -1.0

  # Sort Third 
  l0  =  A[:,2]
  o3p =  B[:,2]
  o3m = -B[:,2]

  l01 = np.dot(o3p-l0,o3p-l0)
  l02 = np.dot(o3m-l0,o3m-l0)
 
  l   = np.array([l01,l02])
  idx = min(range(len(l)), key=l.__getitem__)

  # print idx, l
  if (idx == 1):
    B[:,2] *= -1.0

  return M,B
 
