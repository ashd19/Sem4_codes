sudo tcpdump -i eth0 -c4 
sudo tcpdump -i eth0 -nn 
sudo tcpdump -i eth0 ip6/4
sudo tcpdump -i eth0 -nn src host 192.168.1.5 
sudo tcpdump -i eth0 -nn src net 192.168.1.5 
sudo tcpdump -i eth0 -nn port 21  
sudo tcpdump -i eth0 -nn tcp/udp port 21 
sudo tcpdump -i eth0 tcp/ip/udp
