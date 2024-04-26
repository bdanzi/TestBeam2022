#!/bin/bash

#!/bin/bash

# for dir in `echo 10 11 12 13  14  15  16  17  18  19  20  21  22  23  24  25  26  5 6 7 8 9`; do
for dir in `echo 1 2 4`; do

 echo "Run"$dir

 for eventnumber in `ls Data_OSC_Run${dir}_formatted/ | awk -F '--' '{print $3}' | sed "s?_formatted.txt??g" | sort | uniq`; do  
#for eventnumber in `ls Data_OSC_Run${dir}_formatted/*02424* | awk -F '--' '{print $3}' | sed "s?_formatted.txt??g" | sort | uniq`; do
# for eventnumberoffset in `ls Data_OSC_Run${dir}_formatted/*02424* | awk -F '--' '{print $3","$4}' | sed "s?_formatted.txt??g" | sort | uniq`; do
  # echo "Even" $eventnumberoffset
  # eventnumber=`echo $eventnumberoffset | awk -F "," '{print $1}'`
  # offset=`echo $eventnumberoffset | awk -F "," '{print $2}'`
   echo $eventnumber; 
   rm -f Data_OSC_Run${dir}_formatted/listfiles_Run${dir}_Event${eventnumber}.txt
   ls Data_OSC_Run${dir}_formatted/*${eventnumber}*.txt > Data_OSC_Run${dir}_formatted/listfiles_Run${dir}_Event${eventnumber}.txt
  done

done
