# utils
Frequently used generic (quick and dirty) programs

## python/EigenSystem/EigenSystem.py

*Description*: This program computes the eigensystem (eigenvalues and eigenvector) of a time dependent matrix
``` 
     / A11 A12 A13 \
 A = | A21 A22 A23 |
     \ A31 A32 A33 /
```
This program ensures continuity of the sorted eigenvalues and eigenvectors.

*Usage*: `python EigenSystem.py INPUT`

## awk/Matrix-to-3Cols.awk

*Description*:  This program converts  a matrix written in matrix  form into a 3
columns format (suitable for gnuplot plotting).  If  the matrix has `M` rows and
`N` columns,  then the INPUT file is supossed  to have `M` rows and `N` columns.
The OUPUT file will have `M*(N+1)` rows and 3 columns.

*Usage*: `awk -f 'Matrix-to-3Cols.awk' INPUT > OUTPUT`

## awk/TransposeMatrix.awk

*Description*:  This program  transposes rows and  columns in a  matrix.  If the
INPUT file  has `M` rows  and `N` columns,  then  the OUTPUT file  will have `N`
rows and `M` columns.

*Usage*: `awk -f 'TransposeMatrix.awk' INPUT > OUTPUT`

