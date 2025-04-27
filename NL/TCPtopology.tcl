set ns [new Simulator]

set tracefile [open out.tr w]
$ns trace-all $tracefile

set n0 [$ns node] ;
set n1 [$ns node] 
set n2 [$ns node] ;
set n3 [$ns node] ;
set n4 [$ns node] ;

$ns duplex-link $n0 $n4 1Mb 10ms DropTail
$ns duplex-link $n1 $n4 1Mb 10ms DropTail
$ns duplex-link $n2 $n4 1Mb 10ms DropTail
$ns duplex-link $n3 $n4 1Mb 10ms DropTail


set tcp0 [new Agent/TCP]
$ns attach-agent $n1 $tcp0

set tcp1 [new Agent/TCP]
$ns attach-agent $n2 $tcp1

set tcp2 [new Agent/TCP]
$ns attach-agent $n3 $tcp2


set sink0 [new Agent/TCPSink]
$ns attach-agent $n0 $sink0

set sink1 [new Agent/TCPSink]
$ns attach-agent $n0 $sink1

set sink2 [new Agent/TCPSink]
$ns attach-agent $n0 $sink2


$ns connect $tcp0 $sink0
$ns connect $tcp1 $sink1
$ns connect $tcp2 $sink2


set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0

set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1

set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2


$ns at 1.0 "$ftp0 start"
$ns at 1.5 "$ftp1 start"
$ns at 2.0 "$ftp2 start"


$ns at 10.0 "finish"


proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    exit 0
}


$ns run
