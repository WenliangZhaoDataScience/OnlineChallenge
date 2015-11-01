#! /usr/bin/env bash

cd test
make -f makefile

printf "\n"
./test_run ./data.txt
echo ### Test finished ###

### clean repository
make clean
