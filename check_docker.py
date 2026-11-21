import docker

client = docker.from_env()

running_containers = client.containers.list()

print("-- 目前在干活的容器 --")
print("-- 容器状态监控 --")
for container in running_containers:
        stats = container.stats(stream=False)
        mem_usage = stats['memory_stats']['usage']
        mem_limit = stats["memory_stats"]["limit"]
        mem_usage_mb = mem_usage / (1024 * 1024)
        mem_limit_mb = mem_limit / (1024 * 1024)

        print(f"名字:{container.name}")
        print(f" -> 状态:{container.status}")
        print(f" -> 内存占用:{mem_usage_mb:.2f} MB / {mem_limit_mb:.2f} MB")

        # print(f"名字: {container.name} | 状态: {container.status} | ID: {container.short_id}")
        