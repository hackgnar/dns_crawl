import sys
import dns.resolver #import the module
resolver = sys.stdin.read().strip()
domain = sys.argv[1]
qtypes = ["A","CNAME"]
mdns = dns.resolver.Resolver() #create a new instance named 'myResolver'
mdns.timeout=1
mdns.lifetime=1
mdns.nameservers = [resolver]
try:
    for qtype in qtypes:
        adns = mdns.query(domain, qtype, raise_on_no_answer=False) #Lookup the 'A' record(s) for google.com
        for answer in adns: #for each response
            tmp = ','.join([domain, resolver, qtype, str(answer)]) + '\n'
            sys.stdout.write(tmp)
    sys.stdout.flush()
except:
    pass
