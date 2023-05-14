#!/bin/bash

url = "https://www.flickr.com/search/?text=$1"
echo url
#wget -qO- "https://www.flickr.com/search/?text=$1" | tr -d "\t\n\r" > cars.txt