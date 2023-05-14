#!/bin/bash

wget -qO- "http://bigcharts.marketwatch.com/quickchart/quickchart.asp?symb=$1" | tr -d "\t\n\r" > $1.txt #The wget command is a command line utility for downloading files from the internet, the q prevents it from writing to standard output and makes it silent, O allows me to change the name of the file that is saved to, I then included the link, I then used tr to delete tabs, newlines and returns, and i then transfered all this to a file call stocks.
sed -i 's|.*Last:</span><div>||' stocks.txt #I then used sed to further edit the stocks file, i used -i to edit files in-place, and removing everything before and including that. 
sed -i 's|</div>.*||' stocks.txt | echo '\n' >> stocks.txt #i then also removed the div after the price and and append it to the file
cat stocks.txt #outputs 
