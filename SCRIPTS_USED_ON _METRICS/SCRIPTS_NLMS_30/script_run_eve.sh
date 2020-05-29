#!/bin/bash

for num in {1..30}
do
   echo "=================TESTE $num================="
   timeout 60 python -u eve.py $num 52 & 
   timeout 60 python -u alice.py
done
