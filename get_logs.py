import docker

client = docker.from_env()

db = client.containers.get('my-mysql')

logs = db.logs(tail=100).decode('utf-8')

print("-- 严重警告 --")

lines = logs.split('\n')

for line in lines:
    
    lower_line = line.lower()
    
    if "error" in lower_line or "warning" in lower_line:
    
        print(line)





# logs =db.logs(tail=10)

# print("-- MySQL 启动时的最后 10 行日志 --")

# print(logs.decode('utf-8'))