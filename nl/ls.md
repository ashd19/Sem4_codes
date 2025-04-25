
set ns [new Simulator]


set tf [open out.tr w]
$ns trace-all $tf
set nf [open out.nam w]
$ns namtrace-all $nf

# Create Nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

# Create Links (Assign manual bandwidth/delay to simulate link costs)
$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 20ms DropTail
$ns duplex-link $n0 $n2 1Mb 5ms DropTail

# Set link weights to simulate link-state decision-making
$ns queue-limit $n0 $n1 10
$ns queue-limit $n1 $n2 10
$ns queue-limit $n0 $n2 10

# Setup UDP Traffic from n0 to n2
set udp [new Agent/UDP]
$ns attach-agent $n0 $udp
set null [new Agent/Null]
$ns attach-agent $n2 $null
$ns connect $udp $null

# Application layer: CBR
set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 500
$cbr set interval_ 0.005
$cbr attach-agent $udp

# Start and Stop traffic
$ns at 0.5 "$cbr start"
$ns at 4.5 "$cbr stop"

# Finish Procedure
$ns at 5.0 "finish"

proc finish {} {
    global ns tf nf
    $ns flush-trace
    close $tf
    close $nf
    exec nam out.nam &
    exit 0
}

# Run Simulation
$ns run
