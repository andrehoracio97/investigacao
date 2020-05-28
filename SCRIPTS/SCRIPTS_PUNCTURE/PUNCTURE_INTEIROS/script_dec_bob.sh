#!/bin/bash
 
for num in {1..30}
do
	echo "========================= TESTE $num ========================="
	python -u bob_dec.py $num 3
done
