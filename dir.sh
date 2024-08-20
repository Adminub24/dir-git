#!/bin/bash
size_file() {
    local path="$1"
    local size=$(du -h -s "$path" 2>/dev/null | cut -f1)
   echo $size
}
items=$(ls -A)
for item in $items; do
    size=$(size_file "$item")
    echo -e "$size\t$item"
done | sort -hr -k1,1
