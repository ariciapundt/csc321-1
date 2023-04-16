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


