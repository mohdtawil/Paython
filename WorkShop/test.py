import pprint as pp
p = open('data.txt')
data = p.readlines()
pp.pprint(data)
p.close()
d={}

for e in data:
    l=e.split('\t')
    d[l[0]]=sum([int(l[1]),int(l[2]),int(l[3][:-1])]) 
pp.pprint(d)
with open('r.txt' , 'w') as f:
    for k, v in d.items():
        f.write(k+"\t"+str(v)+'\n')

