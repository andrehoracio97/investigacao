#!/bin/bash

for num in {1..30}
do
	echo "=================TESTE $num================="
   python -u eve_dec.py $num 4
done
