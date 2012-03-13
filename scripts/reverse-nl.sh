#! /bin/bash
# Numérote les lignes dans l'ordre inverse, en finissant par 0

nb=`wc -l chapitre_10-clean.md | cut -c "1-3"`;
nb=$(($nb-1));

while read line;
do
    echo "$nb $line";
    nb=$(($nb-1));
done < chapitre_10-clean.md
