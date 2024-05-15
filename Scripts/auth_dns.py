import os
from tqdm import tqdm


res=os.popen('ls ./outputs').read()
res=res.strip()
res=res.replace('\n',' ')
res=res.split(' ')
#print(res)

progress_bar=tqdm(total=len(list(res)),desc="reverse dns lookups",unit='IP')

for f in res:
    with open(f'./auth_dns_servers/{f}','w'):
        pass


for f in res:
    #print(f'./outputs/{f}')
    file=open(f'./outputs/{f}','r')
    lines=file.readlines()
    #print(f)

    s=set()

    for line in lines:
        if 'SOA' not in line:
            continue
        line=line.strip()
        line=line.replace('\t',' ')
        line=line.split(' ')
        line=line[4]
        s.add(line)
        #print(line)
    #print(s)

    for each in s:
        results=os.popen(f'dig {each} +noall +answer +authority').read()
        results=results.strip()
        results=results.replace('\t',' ')
        #print(results)
        #results=results.split(' ')
        with open(f'./auth_dns_servers/{f}','a') as file:
            file.write(f'{results}\n')
        #print(results)

    #break
    progress_bar.update(1)    
    


# file=open('./outputs/2697.txt','r')
# lines=file.readlines()

# s=set()

# for line in lines:
#     if 'SOA' not in line:
#         continue
#     line=line.strip()
#     line=line.replace('\t',' ')
#     line=line.split(' ')
#     line=line[4]
#     s.add(line)
#     #print(line)
# print(s)

# for each in s:
#     results=os.popen(f'dig {each} +noall +answer +authority').read()
#     results=results.strip()
#     results=results.replace('\t',' ')
#     results=results.split(' ')
#     print(results)
