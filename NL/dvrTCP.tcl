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

set tcp0 [new Agent/TCP]
set sink0 [new Agent/TCPSink]

$ns attach-agent $n0 $tcp0
$ns attach-agent $n2 $sink0
$ns connect $tcp0 $sink0

set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0

$ns at 1.0 "$ftp0 start"
$ns at 5.0 "$ftp0 stop"
$ns at 6.0 "finish"

$ns run
