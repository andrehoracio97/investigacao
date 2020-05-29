#!/bin/bash
 
for num in {1..45}
do
	echo "========================= TESTE $num ========================="
	timeout 60 python -u bob.py $num 72 52
done
