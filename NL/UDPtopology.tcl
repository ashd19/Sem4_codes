set ns [new Simulator]

set nf [open out.nam w]
set np [open out.tr w]
$ns namtrace-all $nf
$ns trace-all $nf


proc finish {} {
    global ns nf np
    $ns flush-trace
    close $nf
    exec nam out.nam &
    exit 0
}


set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]


$ns duplex-link $n0 $n1 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n2 $n3 2Mb 10ms DropTail
$ns simplex-link $n3 $n0 2Mb 10ms DropTail


$ns queue-limit $n0 $n1 5
$ns queue-limit $n1 $n2 5
$ns queue-limit $n2 $n3 5
$ns queue-limit $n3 $n0 5


$ns duplex-link-op $n0 $n1 queuePos 0.5
$ns duplex-link-op $n1 $n2 queuePos 0.5
$ns duplex-link-op $n2 $n3 queuePos 0.5
$ns simplex-link-op $n3 $n0 queuePos 0.5


set udp [new Agent/UDP]
$ns attach-agent $n0 $udp

set null [new Agent/Null]
$ns attach-agent $n3 $null


$ns connect $udp $null


$udp set fid_ 1
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp


$ns at 0.1 "$cbr start"
$ns at 4.0 "$cbr stop"
$ns at 5.0 "finish"


$ns run
