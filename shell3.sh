#!/bin/bash

xterm -e "airodump-ng --bssid $(cat output4.txt) --channel $(cat output5.txt) $(cat output6.txt);bash";
