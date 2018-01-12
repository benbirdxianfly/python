脚本基于单主机单端口，改为单主机多端口监控（原出处没记下来--sorry--）
mdb_sstat.py   具体的执行脚本，放到/usr/local/zabbix/目录下  
mong.xml       zabbix模板，需导入
mongodb.conf   zabbix-agent的配置文件，放入 /etc/zabbix/zabbix_agentd.d/下
qiueer         依赖文件与mdb_sstat.py同一级文件目录