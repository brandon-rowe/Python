#!/bin/bash

echo "Hello World of Bash Scripting"

for i in 1 2 3 4
do
	echo "Number $i"
done

for n in {1..10}
do
	echo "Loop works for test run number $n"
done

#Output the results of a command such as 'ls'

for r in $(ls)
do
	echo $r
done
