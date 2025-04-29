echo "Enter a filename: "
read file

if [ -f "$file" ]; then
    echo "$file exists."
    echo "Counting lines, words, and characters:"
    wc "$file"
else
    echo "$file doesn't exist."
fi

