#  Docker 自动化监控与自愈系统

这是一个基于 Python 和 Docker 开发的企业级基础架构实战项目，旨在实现业务集群的故障自愈与可视化监控。

##  核心功能
- **故障自愈**：Python 脚本全天候巡检，一旦检测到 Nginx 或 MySQL 挂掉，自动在 5 秒内拉起。
- **可视监控**：集成 Prometheus 采集数据，Grafana 展示实时硬件与业务大屏。
- **一键编排**：使用 Docker Compose 实现微服务集群的秒级部署。

##  技术栈
- Python 3.13 (Docker SDK)
- Docker & Docker Compose
- Prometheus & Grafana
- Nginx & MySQL

##  如何运行
1. 确保本地已安装 Docker Desktop。
2. 启动业务集群：`docker-compose up -d`
3. 启动监控大屏：`docker-compose -f docker-compose.monitor.yml up -d`