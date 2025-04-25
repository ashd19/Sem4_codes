the host command is a simple utility used to perform DNS lookups in Unix-like
operating systems. It queries DNS servers to resolve domain names into IP
addresses or vice versa. 
host google.com
host -t ns '' 
hostname
whoami 






1] ifconfig -  used to view and configure network interfaces on Unix/Linux systems 
 used to check IP addresses, MAC addresses, assign ips

 ifconfig eth0
 ifconfig eth0 up
 ifconfig eth0 down 
 ifconfig eth0 192.... 

 ipconfig / release / flush dns / renew - 

2]  traceroute / rt windows -  it traces the routes the packets take to reach the destination 
displaying each hop/router along the way 

traceroute  www.google.com

traceroute -w 200 www.google.com
traceroute will wait 200 milliseconds for each hop before moving on to the next one.
traceroute -n -m 5 www.google.com
-n: Skip DNS resolution; show IP addresses instead of hostnames.

-m 5: Limit the trace to 5 hops.

3] tracepath -  traces the path packets take to
reach a destination, similar to traceroute, but it also measures the Maximum
Transmission Unit (MTU) along the route. It helps identify network issues and
optimize paths by discovering packet size limitations.

tracepath youtube.com
tracepath -help 
'' -4
'' -n show only ip add and skips dns resol 

 Specifies the UDP port number for tracing.
tracepath -p 8080 www.google.com 
Sets the maximum packet size to use during tracing.
tracepath -l 1400 www.google.com
 Limits the trace to a maximum number of hops.
tracepath -m 10 www.google.com
Displays the hop number for each hop.
tracepath -h www.google.com
tracepath -v www.google.com - detailed info 
tracepath -w 300 www.google.com - wait time for each hop reply 

4] ping  -  used to test the reachability of a host and measure the round-
trip time for messages sent to the destination
ping -c 4 www.google.com - no. of ping reqs to send 
 Sets the interval (in seconds) between sending each packet.
ping -i 1 www.google.com

 Sets the TTL (Time To Live) for the packet.
ping -t 64 www.google.com

Sets the size of the ping packet (in bytes).
ping -s 100 www.google.com
Shows numerical output (doesn't resolve hostnames to IP addresses).
ping -n www.google.com 
-l

    Description: Sends a large buffer size (in bytes) in the ping request.

    Example:

    ping -l 1500 www.google.com
-R
    Description: Records the route taken by the ping packets (Unix-based systems).
   ping -R www.google.com

-q
    Description: Suppresses most output and shows only the summary.
    ping -q www.google.com
-W
    Description: Sets the timeout in seconds for each ping request.
ping -W 2 www.google.com
