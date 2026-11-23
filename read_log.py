#定义日志文件的路径（windows读取自己的D盘文件用D:\开头）
log_path = r"D:\pythonDocker\linux-text\disk_history.log"

print("-- 正在扫描传来的日志 --")

try:
    # 打开文件进行读取
    with open(log_path, "r", encoding='utf-8') as file:
        for line in file:
            #如果这一行有“快满了”关键词
            if "快满了" in line:
                print(f"！！抓到异常！报警内容：{line.strip()}")

    print("--扫描结束--")
except FileNotFoundError:
    print("找不到日志文件，请检查路径！ ")