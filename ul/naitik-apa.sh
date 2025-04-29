#!/usr/bin/perl
use strict;
use warnings;

my %students = (
    "Naitik"  => 56,
    "Atharva" => 53,
    "Ashton" => 27,
    "Tarun"  => 45,
    "Rishit"   => 57
);

#user input
print "Enter student name: ";
my $name = <STDIN>;
chomp($name);

if (exists $students{$name}) {
    print "Roll number of $name: $students{$name}\n";
} else {
    print "Student not found!\n";
}
