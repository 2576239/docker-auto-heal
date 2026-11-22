#!/bin/bash
# 获取 / 目录的磁盘使用百分比（去掉百分号只留下数字）
disk_usage=$(df -h /mnt/c | awk 'NR==2 {print $5}' | tr -d '%')

echo "当前磁盘使用率: ${disk_usage}%"

# 如果使用率大于 80，就发出警告
if [ $disk_usage -gt 80 ]; then
	echo "磁盘空间快满了"
else
	echo "磁盘空间很健康"
fi

