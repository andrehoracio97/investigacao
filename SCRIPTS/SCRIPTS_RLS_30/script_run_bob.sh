#!/bin/bash
 
for num in {1..30}
do
	echo "========================= TESTE $num ========================="
	timeout 120 python -u bob.py $num 72 52
done
