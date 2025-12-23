filesize=$(stat -c%s firmware.BIN)
window=65536
for ((off=0; off<filesize; off+=window)); do
  count=$(dd if=firmware.BIN bs=1 skip=$off count=$window 2>/dev/null | strings -n 4 | wc -l)
  printf "offset=0x%X count=%d\n" $off $count
done
