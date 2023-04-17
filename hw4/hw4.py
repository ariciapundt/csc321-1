import socket
import pandas as pd
import csv
import graphviz

mainDom = 1
dns = {}
last = {}
dom = pd.read_csv("domains.tsv", sep = '\t')['domain']#read domains
dict = {}
addr = {}
node =300

#forward DNS
#try:

    #ip_addr = socket.gethostbyname(website)
    #print(f'{website}:{ip_addr}')
#except:
    #pass
    
#REVERSE dns lookup
#for websites in websites:
    #try:
        #ip_addresses = socket.getaddrinfo(website, None)
       # for ip_addr in ip_addresses:
          #  reverse_dns = socket.gethostbyaddr(ip_address[4][0])
           # print(f'IP address {ip_addr[4][0]} is associated with {reverse_dns[0]}')
  #  except: pass
    
    
dot = graphviz.Digraph(engine='fdp', comment='digraphtesting')

for i in dom:
    try:
        address = socket.getaddrinfo(dom, 443, type=socket.SOCK_STREAM)#forward dns
    except:
        pass
mainDom = mainDom + 1
with dot.subgraph() as s:
    s.node(str(mainDom), i)
for j in range(len(address)-1):
    try:
        port = address[j][4]
        rev_dns = socket.gethostbyaddr(port[0])[0]#reverse DNS
    except:
        pass
node = node +1
dot.node(str(node), rev_dns)
dot.edge(str(node), str(mainDom))


