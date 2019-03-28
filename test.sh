#!/bin/bash
sudo apt-get install -y python-dnspython
curl -L -O https://opendata.rapid7.com/sonar.udp/2019-02-04-1549285686-udp_dns_53.csv.gz
gunzip 2019-02-04-1549285686-udp_dns_53.csv.gz
for i in $(awk -F',' '{print $2}' ../2019-02-04-1549285686-udp_dns_53.csv); do printf "%q\n" "echo -n $i | python dns_crawl.py trello.com >> results.csv"; done | xargs -I CMD --max-procs=500 bash -c CMD
