echo "Enter a number: "
read number
echo "Number entered: $number"
if ((number%2 == 0)); then
	echo "$number is even."
else
	echo "$number is odd."
fi
