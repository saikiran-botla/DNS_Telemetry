import os
import pandas as pd
import ipaddress
import socket
from tqdm import tqdm

import argparse


parser=argparse.ArgumentParser()

parser.add_argument("-i","--input", help="Show Input")
parser.add_argument("-t","--trace",help="Show trace")
args=parser.parse_args()


df=pd.read_csv(f'{args.input}')

progress_bar=tqdm(total=len(list(df.iterrows())),desc="reverse dns lookups",unit='IP')


a=0

asns=list(set(df['asn']))

for each in asns:
    with open(f'./outputs_trace/{each}.txt','w'):
        pass


for idx, row in df.iterrows():
    ip=row['ipv4']
    asn=row['asn']
    ip=ip.strip('')
    ip=ip.split('/')[0]
    try:
        tr=args.trace
        result=os.popen(f'dig -x {ip} +noall +answer +authority +trace').read()
        with open(f'./outputs_trace/{asn}.txt','a') as file:
            file.write(f'{ip}\n {result} \n')
    except:
        result=os.popen(f'dig -x {ip} +noall +answer +authority').read()
    #print(asn,":",result)
        with open(f'./outputs/{asn}.txt','a') as file:
            file.write(f'{ip}\n {result} \n')
    #os.system(f'dig -x {ip} +noall +answer +authority >> output.txt')
    progress_bar.update(1)
    



    
    
    
    



