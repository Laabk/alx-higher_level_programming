#!/bin/bash
# A bash script to get the size  of the body response
curl -s "$1" | wc -c
