#!/bin/bash

for num in {1..30}
do
   echo "=================TESTE $num================="
   timeout 120 python -u eve.py $num 52 & 
   timeout 120 python -u alice.py
done
