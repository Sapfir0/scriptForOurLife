#!/bin/bash

find . -not -path "./node_modules/*" -not -path "./public/img/*" -not -path "./.git/*" -not -path "./public/js/ckeditor/*" -not -name "package*" -type f | xargs wc -l   
 
