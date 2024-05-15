import os
from tqdm import tqdm

import argparse


parser=argparse.ArgumentParser()

parser.add_argument("-i","--input", help="Show Input")
parser.add_argument("-o","--option", help="Show Input")
args=parser.parse_args()


file=open(f'{args.input}','r')

lines=file.readlines()

with open("primary_name_servers.csv",'w'):
    pass

with open("primary_name_servers.csv",'+a') as f:
    f.write("domain,primary_dns,email\n")


progress_bar=tqdm(total=len(list(lines)),desc="processing...",unit='IP')


for line in lines[1:]:
    line=line.strip()
    if 'www' in line:
        continue
    line=line[2:]
    try:
        res=os.popen(f'dig {args.option} {line} +noall +answer +authority').read()
        res=res.strip()
        res=res.replace('\t',' ')
        res=res.replace('  ',' ')
        res=res.split(' ')
        res=res[0] +","+ res[4] + ","+ res[5]+"\n"


        with open('primary_name_servers.csv','a') as f:
            f.write(res)

    except:
        pass

    
    progress_bar.update(1)
    
    #print(line)
