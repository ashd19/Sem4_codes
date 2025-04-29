
use strict;
use warnings;

print "Enter length: ";
my $length = <STDIN>;
chomp($length);

print "Enter breadth: ";
my $breadth = <STDIN>;
chomp($breadth);

my $area = $length * $breadth;
my $perimeter = 2 * ($length + $breadth);

print "Area: $area\n";
print "Perimeter: $perimeter\n";
