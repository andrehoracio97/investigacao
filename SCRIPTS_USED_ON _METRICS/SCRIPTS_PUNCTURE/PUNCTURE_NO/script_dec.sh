#!/bin/bash

for num in {1..45}
do
	echo "=================TESTE $num================="
   python -u eve_dec.py $num
done
