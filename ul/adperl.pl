#!/usr/bin/perl
use strict;
use warnings;

my %heights=(
"ash"=>120,
"raj"=>1290,
);

print "Enter the name of the person of whom u want to know the name of : ";
chomp(my $name= <STDIN>);

if(exists $heights{$name}){
print "The height of ${name} is $heights{$name}";
}
else{
print "Invalid"
}