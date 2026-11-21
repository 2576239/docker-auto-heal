import docker
import time

client = docker.from_env()
container_name = 'my-web-custom'

print(f"赛博保安，全天监控{container_name}...")
print("(去docker desktop 里手动停，看看会发生什么)")

while True:
    try:
        target = client.containers.get(container_name)

        # 如果挂了状态不是running
        if target.status != 'running':
            print(f"\n [警报] {time.strftime('%H:%M:%S')} - 发现{container_name} 意外死亡！ ")
            print("[执行] 正在自动重启容器...")
            target.start()
            print("[结果] 重启成果，继续自动检测中...\n")

        else:
            # 如果活着，就打印提示，证明在巡检
            print(f"[{time.strftime('%H:%M:%S')}] 状态正常...")

    except docker.errors.NotFound:
        print(f"\n [严重错误] 找不到容器{container_name} 时间 {time.strftime('%Y-%m-%d, %H:%M:%S')}")

    time.sleep(5)

