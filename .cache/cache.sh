#!/bin/bash
while true; do
if [[ -s .temp_cashu.txt ]]; then
exit
else
    awk -F 'Time: | ID:' '{print $2}' .pend.txt > .timestamps.txt
    sort -r .timestamps.txt > .sorted_timestamps.txt
    timestamp=$(head -n 1 .sorted_timestamps.txt)
    grep -A '2' "$timestamp" .pend.txt | grep -v "$timestamp" | head -n 2 | awk 'NF' > .temp_cashu.txt
    shred -u .timestamps.txt .sorted_timestamps.txt
fi
done
