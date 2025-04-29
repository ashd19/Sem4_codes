#!/usr/bin/perl
use strict;
use warnings;

print "Enter a number: ";
my $num = <STDIN>;
chomp($num);

my $abs_num = abs($num);
print "Absolute value: $abs_num\n";

print "Multiplication table of $abs_num:\n";
for my $i (1..10) {
    print "$abs_num x $i = " . ($abs_num * $i) . "\n";
}
