# 使用 Maven 官方镜像作为构建阶段
FROM maven:3.8.4-openjdk-17-slim AS builder

# 设置工作目录
WORKDIR /app

# 复制 pom.xml 和源代码
COPY pom.xml .
COPY src ./src

# 构建应用
RUN mvn clean package -DskipTests

# 使用轻量级 JDK 镜像作为运行时
FROM openjdk:17-slim

# 设置工作目录
WORKDIR /opt/manager-api

# 从构建阶段复制 JAR 文件
COPY --from=builder /app/target/*.jar app.jar

# 暴露端口
EXPOSE 8080

# 添加健康检查
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

# 设置启动命令
ENTRYPOINT ["java", "-jar", "app.jar"] 