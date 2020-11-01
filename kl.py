
lstn=[]
lst =[]
lst1=[]
lst2=[]
lst3=[]
lst4=[]
print("Enter Name of Peoples")
for i in range ( 0, 5):
    ele = input ()
    lstn.append ( ele )

print("Enter Age,Phone of ",lstn[0])
for i in range ( 0, 2):
    ele = int(input ())
    lst.append ( ele )

print("Enter Age,Phone of ",lstn[1])
for i in range ( 0, 2 ):
    ele = int( input () )
    lst1.append ( ele )

print("Enter Age,Phone of ",lstn[2])
for i in range ( 0, 2 ):
    ele = int( input () )
    lst2.append ( ele )

print("Enter Age,Phone of ",lstn[3])
for i in range ( 0, 2 ):
    ele = int( input () )
    lst3.append ( ele )

print("Enter Age,Phone of ",lstn[4])
for i in range ( 0, 2 ):
    ele = int( input () )
    lst4.append ( ele )

if (lst[0]>=18):
    print(lstn[0],"is eligeble for voting")
if (lst1[0]>=18):
    print(lstn[1],"is eligeble for voting")
if (lst2[0]>=18):
    print(lstn[2],"is eligeble for voting")
if (lst3[0]>=18):
    print(lstn[3],"is eligeble for voting")
if (lst4[0]>=18):
    print(lstn[4],"is eligeble for voting")

