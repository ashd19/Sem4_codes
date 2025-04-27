set ns [new Simulator]

set nf [open out.nam w]
set tf [open out.tr w]
$ns namtrace-all $nf
$ns trace-all $tf

proc finish {} {
    global ns nf tf
    $ns flush-trace
    close $nf
    close $tf
    exec nam out.nam &
    exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]


$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n0 $n2 2Mb 20ms DropTail


$ns rtproto DV


set udp0 [new Agent/UDP]
set null0 [new Agent/Null]

$ns attach-agent $n0 $udp0
$ns attach-agent $n2 $null0
$ns connect $udp0 $null0

set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp0
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.5


$ns at 1.0 "$cbr0 start"
$ns at 5.0 "$cbr0 stop"
$ns at 6.0 "finish"


$ns run
