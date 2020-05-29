#!/bin/bash

for num in {1..45}
do
   echo "=================TESTE $num================="
   timeout 60 python -u eve.py $num 60 & 
   timeout 60 python -u alice.py 3
done
