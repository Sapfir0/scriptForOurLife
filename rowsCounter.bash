#!bin/bash

find . -not -path "./node_modules/*" -not -path "./.git/*" -not -name "package*" -type f | xargs wc -l   
