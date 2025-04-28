# Write a shell script to create a c program with name as your
# 'firstname.c', compile it as an executive file 'firstname.exe', pass
# parameter as your roll number and run it to display:
# "I, firstname lastname, roll number 'num' wish you a very happy holi"
#cat is mainly used to:
# Display the contents of a file.
# Create a new file.
# Concatenate (join) files together. 
# sudo apt update
# sudo apt install gcc                               #!/bin/bash
# fname="ashton"
# lname="Dsouza"

# cat>"$fname.c"<<EOF
# #include <stdio.h>
# int main(int argc,char *argv[]){
# printf("I, %s %s roll no %s wish happy birthday\n","$fname","$lname",argv[1]);
# return 0;
# }
# EOF
# gcc "$fname.c" -o "$fname.exe"
# ./"$fname.exe" "$1"


#----------------------------

#   GNU nano 7.2                                   adshell.sh                                             #!/bin/bash
# days=("MON" "TUE" "WED" "THURS" "FRI" "Sat" "Sun")

# echo "days = MON,TUE,WED,THURS,FRI,Sat,Sun"
# echo "Enter the index of the day u want to print"
# read index

# if [[ $index -ge 0 && $index -le 6 ]]; then
# echo "The day at index $index is : ${days[index]}"
# else
# echo "Invalid index"
# # fi
 
#    GNU nano 7.2                                  basicperl.sh                                            #!/bin/bash
# surnames=("a" "b" "c" "d")
# read index
# if [[ $index -ge 0 && $index -le 3 ]]; then
# echo "EXISTS"
# else
# echo "NO"
# fi

echo $arr[@]



