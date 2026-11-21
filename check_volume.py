import docker

client = docker.from_env()
print("---正在查看Docker数据卷---")
volumes = client.volumes.list()
for vol in volumes:
    print(f"卷名：{vol.name}")