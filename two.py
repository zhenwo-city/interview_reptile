import pandas as pd
pr=pd.read_csv(r'C:\Users\库\Downloads\fyx_chinamoney.csv',header=None)
list_len=int(pr.__len__()/80+1)
print(list_len)
arr=[]
zidian={}
for i in range(0,list_len):
    print(i)
    for j in range(0,80):
        print("j",j)
        if(i*80+j==500):
            break
        arr.append(pr[0][i*80+j])
    list_name=F'List{i}'
    zidian.update({list_name:arr})
    arr=[]
print(zidian)
