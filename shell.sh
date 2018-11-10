#!/usr/bin/bash

sudo airmon-ng > output.txt;
awk '{print $1 " "}' output.txt > output1.txt; 
