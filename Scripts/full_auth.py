import os
from tqdm import tqdm

res=os.popen('ls ./auth_dns_servers').read()
res=res.strip()
res=res.replace('\n',' ')
res=res.split(' ')
#print(res)

progress_bar=tqdm(total=len(list(res)),desc="scanning for node data",unit='IP')

# for f in res:
#     with open(f'./node_data/{f}','w'):
#         pass

s=set()



for f in res:
    #print(f'./outputs/{f}')
    file=open(f'./auth_dns_servers/{f}','r')
    lines=file.readlines()
    #print(f)

    for line in lines:
        line=line.strip()
        line=line.split(' ')
        dns=line[0]
        dns=dns.split('.')
        dns=dns[1:-1]
        #print(dns)
        domain=''
        for each in dns:
            domain+=each+"."
        #print(domain)
        s.add(domain)
        #res=os.popen(f'dig ns {dns} +noall +answer +authority').read()
        #print(res)
    #break

    progress_bar.update(1)  

for each in s:
    print(each)
