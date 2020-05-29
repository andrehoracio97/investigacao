#!/bin/bash

for num in {1..45}
do
   echo "=================FICHEIRO $num================="
   cp $num/EVE_55_8000.txt threshold2/$num 
done
