#!/bin/bash

## Set root path for exploits
root_path="../modules/exploits/"

## Get overall rankings
grep -R "Rank =" $root_path \
    | awk {'print $4'} \
    | sort -nr \
    | uniq -c \
    | awk '{printf "%-18s,%s\n", $2, $1}' > overall_rankings

## Get overall platform exploits
grep -R "Rank =" $root_path \
    | awk {'print $1'} \
    | grep -o -P "(?<=$root_path).*?(?=/)" \
    | sort -nr \
    | uniq -c \
    | awk '{printf "%-12s,%s\n", $2, $1}' > overall_exploits

## Not filter all platforms
cat overall_exploits | while read line ; do
    sub_path=$(echo $line | awk {'print $1'}) && mkdir -p $sub_path
    search_path="$root_path$sub_path"

    grep -R "Rank =" $search_path \
        | awk '{print $4'} \
        | sort -nr \
        | uniq -c \
        | awk '{printf "%-18s,%s\n", $2, $1}' > $sub_path/platform_result
done
