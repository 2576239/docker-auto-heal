import docker
import time

client = docker.from_env()
container_name = 'my-web-custom'

try:

    target = client.containers.get(container_name)
    print(f" 【发现目标】{container_name} 当前状态是: {target.status}")

    if target.status == 'running':
        print("【执行】正在下达停止指令..")
        target.stop()
        print("网页已停止")

        print("【等待】 休眠5秒,刷新浏览器，,,")
        time.sleep(5)

    if target.status != 'running':
        print("【执行】 正在唤醒，，")
        target.start()
        print("【结果】 已复活，刷新浏览器，，")

except docker.errors.NotFound:
    print(f"【报错】 找不到叫 {container_name} 的容器，，，")