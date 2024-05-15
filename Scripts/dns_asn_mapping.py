import os
from tqdm import tqdm
from ipwhois import IPWhois
import argparse


parser=argparse.ArgumentParser()

parser.add_argument("-i","--input", help="Show Input")
args=parser.parse_args()

def get_asn(ip):
    obj = IPWhois(ip)
    result = obj.lookup_rdap()

    return result['asn']

# print(get_asn('10.0.160.80'))
# exit()

file=open(f'{args.input}','r')

lines=file.readlines()

a=0

with open('dns_asn_mapping.csv','w'):
    pass

with open('dns_asn_mapping.csv','+a') as file:
    file.write('domain, dns_server, ip, asns\n')


progress_bar=tqdm(total=len(list(lines)),desc="scanning for node data",unit='IP')
for line in lines:
    line=line.strip()
    line=line.replace('\t',' ')
    while '  ' in line:
        line=line.replace('  ',' ')
    line=line.split(' ')
    print(line)
    
    domain=line[0]
    domain_dns=line[4]
    #print(f'dig {domain_dns} +noall +answer')

    try:
        res=os.popen(f'dig {domain_dns} +noall +answer').read()
        #print(domain_dns,res)
        res=res.strip()
        res=res.replace('\t',' ')
        while '  ' in res:
            res=res.replace('  ',' ')
        res=res.split(' ')
        #print(res[4])
        
        ip=res[4]
        asn=get_asn(ip)
        
        with open('dns_asn_mapping.csv','+a') as file:
            file.write(f'{domain}, {domain_dns}, {ip}, {asn}\n')
    #print(domain,domain_dns,ip,asn)
    except:
        with open('dns_asn_mapping.csv','+a') as file:
            file.write(f'{domain}, {domain_dns}, , \n')

    progress_bar.update(1)

    #print(domain,domain_dns)
    
    