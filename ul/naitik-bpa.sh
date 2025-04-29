use strict;
use warnings;
my @months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");


print "Enter a number (1-12) to get the month name: ";
my $num = <STDIN>;
chomp($num);

if ($num >= 1 && $num <= 12) {
    print "The month is: $months[$num - 1]\n";
} else {
    print "Invalid input! Please enter a number between 1 and 12.\n";
}
