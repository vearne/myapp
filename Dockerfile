FROM dockerfile/python

VOLUME ["/var/run/supervisor"]

RUN pip install tornado==4.5.1 supervisor
## 使用supervisor来管理我们的服务
## 可以做服务拉起，即使程序失败退出，也可以保留现场
COPY supervisord.conf /etc/
COPY myapp.ini /etc/supervisord.d/
COPY server.py /data/

## 让supervisord运行在前台，阻止docker容器退出
CMD ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]




