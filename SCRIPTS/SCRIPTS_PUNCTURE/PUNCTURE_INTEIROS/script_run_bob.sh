#!/bin/bash
 
for num in {1..30}
do
	echo "========================= TESTE $num ========================="
	timeout 60 python -u bob.py $num 74 50
done
