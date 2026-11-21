import subprocess

print("【执行】正在启动所有容器群...")
result = subprocess.run(["docker-compose","up","-d"], capture_output=True, text=True)

if result.returncode == 0:
    print("集群启动成功！")
else:
    print("启动失败，报错信息如下：")
    print(result.stderr)