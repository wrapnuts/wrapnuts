#!/bin/bash
cashu pending | cat > .pend.txt
sed -n '5~6p' .pend.txt > .c.list
while IFS= read -r line; do cashu receive "$line" >> output.txt; done < .c.list
shred -u .pend.txt output.txt .c.list
