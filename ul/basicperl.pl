#!/usr/bin/perl
use strict;
use warnings;
use Math::Trig;

print "Enter radius of the cone: ";
chomp(my $radius = <STDIN>);

print "Enter height of the cone: ";
chomp(my $height = <STDIN>);

if ($radius > 0 && $height > 0) {
    my $volume = (1/3) * pi * $radius**2 * $height;
    printf "Volume of the cone is: %.2f cubic units\n", $volume;
} else {
    print "Invalid input. Please enter positive numbers for radius and height.\n";
}
