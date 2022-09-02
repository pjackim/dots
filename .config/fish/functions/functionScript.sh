#!/bin/bash

echo -n "name: "
read name

echo -n "command: "
read cmd

echo -n "args: "
read arg


fileName="$name.fish"
touch $fileName

echo "function $name" > $fileName

if [[ $cmd == "cd" ]]
then
    arg="$HOME/$arg"
fi 

echo "    $cmd $arg \$argv" >> $fileName
echo "end" >> $fileName
