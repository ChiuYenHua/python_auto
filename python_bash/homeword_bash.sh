#!/bin/bash
> oldFiles.txt
files=$(grep ' jane ' ~/data/list.txt | cut -d' ' -f3)
#echo $files

for file in $files; do
  if test -e ..$file;
  then echo $file>>oldFiles.txt;
  else echo "File doesn't exist";
  fi
done
