 nl=[]
  for x in range(1000, 2000):
    if (x%11==0) and (x%6!=0):
        nl.append(str(x))
    print (','.join(nl))
