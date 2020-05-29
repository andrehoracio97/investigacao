#!/bin/bash
 
for num in {1..45}
do
	echo "========================= TESTE $num ========================="
	python -u bob_dec.py $num
done
