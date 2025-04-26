# Create a simulator object
set ns [new Simulator]

# Create a trace file
set tracefile [open bus_topology.tr w]
$ns trace-all $tracefile

# Create nodes
for {set i 0} {$i < 5} {incr i} {
    set n($i) [$ns node]
}

# Connect nodes in a bus-like linear fashion
for {set i 0} {$i < 4} {incr i} {
    $ns duplex-link $n($i) $n([expr $i+1]) 1Mb 10ms DropTail
}

# Set up a simple communication (e.g., n0 sends to n4)
set udp [new Agent/UDP]
$ns attach-agent $n(0) $udp

set null [new Agent/Null]
$ns attach-agent $n(4) $null

$ns connect $udp $null

set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 500
$cbr set interval_ 0.005
$cbr attach-agent $udp

# Schedule events
$ns at 0.5 "$cbr start"
$ns at 4.5 "$cbr stop"
$ns at 5.0 "finish"

# Define finish procedure
proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    exec nam bus_topology.nam &
    exit 0
}

# Run the simulation
$ns run