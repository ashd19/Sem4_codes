use strict;
use warnings;

my %students;
my $max_name = "";
my $max_marks = -1;

for (my $i = 1; $i <= 5; $i++) {
    print "Enter name of student $i: ";
    chomp(my $name = <STDIN>);
    
    print "Enter marks for $name: ";
    chomp(my $marks = <STDIN>);
    
    $students{$name} = $marks;
    
    if ($marks > $max_marks) {
        $max_marks = $marks;
        $max_name = $name;
    }
}

print "\nStudent with highest marks: $max_name ($max_marks)\n";
