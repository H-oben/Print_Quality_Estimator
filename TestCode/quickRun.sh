#!/bin/bash

echo 'Running all tests, requires python 3, ensure the correct environment is being used'
echo ''
python3 testSize.py
echo ''
python3 testBurns.py
echo ''
python3 testElephant.py
echo ''
echo 'Finished all tests'
