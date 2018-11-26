# 数据库: 存储数据的仓库


# sql语句规范
# mysql -h远程地址 -P端口号 -u用户名 -p密码
# sql命令不区分大小写, 最后加 ; 号

###############库##########################
# create database [if not exists] db_name [character set 编码];  # 创建数据库
# show databases;  # 查看数据库
# show warnings;  # 查看警告内容
# show create database db_name;  # 查看库信息
# drop database db_name;  # 删除库
# alter database db_name character set 编码;  # 修改数据库编码
# use db_name;  # 进入数据库
# select database();  # 查看当前所在数据库 

# 主键: 非空且唯一, not null unique

########################表#######################
# create table [if not exists] table_name [character set 编码]