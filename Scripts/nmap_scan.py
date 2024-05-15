import os
from tqdm import tqdm

res=os.popen('ls ./auth_dns_servers').read()
res=res.strip()
res=res.replace('\n',' ')
res=res.split(' ')
#print(res)

#progress_bar=tqdm(total=len(list(res)),desc="scanning for node data",unit='IP')

for f in res:
    with open(f'./node_data/{f}','w'):
        pass


i=0
os.system("echo '' > status.txt")
for f in res:
    #print(f'./outputs/{f}')
    i+=1
    os.system(f'echo scanning {f} >> status.txt')
    file=open(f'./auth_dns_servers/{f}','r')
    lines=file.readlines()
    #print(f)

    s=set()

    for line in lines:
        line=line.strip()
        line=line.split(' ')
        dns=line[0]
        ip=line[-1]

        results=os.popen(f'nmap -A -Pn {ip}').read()
        with open(f'./node_data/{f}','a') as file:
            file.write(f'{dns}\n{results}')

    os.system(f'echo done {f} {i}/{len(res)} >> status.txt')
    #progress_bar.update(1)    

