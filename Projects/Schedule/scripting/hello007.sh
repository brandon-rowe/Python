#!/bin/bash
#Hello Agent 007

echo "Hello 007"

for i in $(cat ~/Desktop/todo.txt)
do
	echo $i
done
