import docker

client = docker.from_env()

print("-- 正在扫描 Docker 局域网 --")
# 获取所有网络列表
networks = client.networks.list()

for net in networks:
    #只打印名字带 default 的网络，过滤掉系统自带的
    if "default" in net.name:
        print(f"网络名称：{net.name}")
        print(f"网络ID: {net.short_id}")
        print("-" * 20)
