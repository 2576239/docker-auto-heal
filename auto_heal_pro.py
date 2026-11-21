import docker
import time

client = docker.from_env()
container_name = 'my-web-custom'
log_file = 'heal_history.txt'  # 记录到文本
print(f" 赛博保安升级版，正在全天候监控{container_name}...")

while True:
    try:
        target = client.containers.get(container_name)
        if target.status != 'running':
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            # 打开文件，追加记录
            with open(log_file,'a',encoding='utf-8') as f:
                f.write(f"[{current_time}] 警报 容器意外死亡，已执行重启。 \n")
            print(f" ! [{current_time}] 发现异常，已记录到文件并重启容器...")
            target.start()
        else:
            print(f"[{time.strftime('%H:%M:%S')}] 状态正常...")    
    except docker.errors.NotFound:
        print(f"\n ! [严重错误] 找不到容器 {container_name}")
    time.sleep(5)