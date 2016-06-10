BEGIN{i=1}
{
  for (j=1;j<=NF;j++)
    print i,j,$j  
  i++
  print ""
}
END{}
