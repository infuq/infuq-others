1.第一步编译和执行
python run.py

2.执行以下命令查看committed和已使用内存
查看进程11557的committed内存
i=0;while true; do echo $((i++)) $(pmap -d 11557  |  tail -1); sleep 2; done
查看进程11557已使用内存
i=0;while true; do echo $((i++)) $(/mnt/d/Repository/infuq-others/Lab/tools/smem-1.4/smem -t -k  | tail -3 | head -1); sleep 2; done
