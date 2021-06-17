> oldFiles.txt

files=$(grep 'jane' list.txt | cut -d' ' -f3)
#echo $files

for file in $files; do
  echo $file
  if test -e $file;
  then echo $file>>oldFiles.txt;
  else echo "File doesn't exist";
  fi
done
#jane_profile_07272018.doc
#if test -e jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
