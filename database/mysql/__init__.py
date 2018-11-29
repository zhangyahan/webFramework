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
############################################
# 主键: 非空且唯一, not null unique

########################表#######################
# create table [if not exists] table_name [character set 编码]
# show create table table_name;  # 查看表信息
# desc table_name;  # 查看表结构
# drop table table_name;  # 删除表名
# insert into 表名 values(值1),(值2);  # 插入表信息
# insert into 表名(字段1,..) values(值1),...;  # 插入表信息(指定字段)
# select * from 表名 [where 条件];  # 查询表记录
# select 字段1,字段2 表名 [where 条件];  # 查询表信息(指定字段)
# alter table 表名 add 字段名 数据类型;  # 添加表字段
# alter table 表名 add 字段名 数据类型 first;  # 插到第一位
# alter table 表名 add 字段名 数据类型 after 字段名1;  # 指定插到字段1后
# alter table 表名 drop 字段名;  # 删除表字段
# alter table 表名 modify 字段名 新数据类型;  # 修改数据类型
# alter table 表名 rename 新表名;  # 修改表名
# delete from 表名 where 条件;  # 删除符合条件的表记录
# update 表名 set 字段=值 where 条件;  # 修改符合条件的表记录


#########################数据类型######################
# 数值类型
# 整型
# int        大整型(4个字节)
# tinyint    微小整型(1个字节)
#   有符号(signed默认): -128~127  无符号(unsigned): 0~255
# smallint   小整型(两个字节)
# bigint     极大整型(8个字节)
# 浮点型
# float(m,n)  四个字节,最多显示7个有效位
# decimal(m,n)  最多显示28个有效位
#
# 字符类型
# char        定长(1~255)
# varchar     变长(1~65535)
# text/longtext/blob/longblob
# 字符类型宽度和数值类型宽度的区别
# 数值类型宽度为显示宽度,只能用于select查询显示,和占用存储无关,
# 可用zerofill查看效果
# 字符类型的宽度超过之后则无法存储
#
# 枚举类型
# 单选(enum): 字段名 enum(值1,值2,..)
# 多选(set):  字段名 set(值1,值2,..)
## 插入数据时: 'F,study,Python'
#
# 日期时间类型
# date: "YYYY-MM-DD"
# time: "HH:MM:SS"
# datetime: "YYYY-MM-DD HH:MM:SS"
# timestamp: "YYYY-MM-DD HH:MM:SS"
# 注意: datetime不给值默认返回NULL值
#      timestamp不给值返回系统当前时间
# 时间日期函数
# now(): 返回服务器当前时间
# curdate(): 返回当前日期
# curtime(): 返回当前时间
# year(date): 返回指定时间的年份
# date(date): 返回指定时间的日期
# time(date): 返回指定时间的时间
# 日期时间运算
# select * from 表名
# where 字段名 运算符 (时间-interval 时间间隔单位)
# 时间间隔单位
# day | hour | minute | year | mouth
# 1、查询1天以内的记录
#       select * from t7 
#       where shijian > (now()-interval 1 day);
#     2、查询1年以前的记录
#       select * from t7
#       where shijian < (now()-interval 1 year);
#     3、查询1天以前,3天以内的记录
#       select * from t7
#       where
#       shijian < (now()-interval 1 day) and
#       shijian > (now()-interval 3 day);



##################运算符##################
# 数值字符比较
# = != < <= > >=
# 逻辑比较
# and  or
# 范围比较
# between 值1 and 值2
# where 字段名 in (值1,...)
# where 字段名 not in (值1,...)
# 匹配空, 非空
# is null not is null
# NULL: 空值,只能用is或not is去匹配
# "": 空字符串,用=或!=去匹配
# 模糊比较
# where 字段名 like 表达式
# 表达式
# _ 匹配单个字符
# % 匹配0到多个字符


##################sql查询#################
# 3.select ...聚合函数 from 表名
# 1.where ...
# 2.group by ...
# 4.having ....
# 5.order by ...
# limit ...
#
# order by
# 给查询记过进行排序
# ... order by 字段名 ASC/DESC
#
# limit(永远放在SQL语句的最后,限制显示查询记录的个数)
# limit n : 显示n条
# limit m,n : 从m+1开始显示n条
# 分页 m(页), n(条)
# 公式 limit(m-1)*n, n
#
# 聚合函数
# avg(字段名): 求平均值
# sum(字段名): 求和
# max(字段名): 最大值
# min(字段名): 最小值
# count(字段名): 统计该字段记录的个数
# 
# group by
# 对查询结果进行分组
# select 字段1,avg(字段2) from 表名 group by 字段1;
# 分组的条件必须在查询的字段中
# 先分组 在聚合 在去重
#
# having
# 对查询的结果进行进一步筛选
# 找出平均攻击力>105的国家的前2名,显示国家名和平均攻击力
#    select country,avg(gongji) as pjgj from sanguo
#    group by country
#    having pjgj>105
#    order by pjgj DESC
#    limit 2;
# having语句通常和group by语句联合使用,过滤由group by语句返回的记录集
# where只能操作表中实际存在字段,having可操作由聚合函数生成的显示列
#
# distinct
# 作用 ：不显示字段重复值
# 表中都有哪些国家
# select distinct country from sanguo;
# 计算蜀国一共有多少个英雄
# select count(distinct id) from sanguo 
# where country="蜀国";
# distinct和from之间所有字段都相同才会去重
# distinct不能对任何字段做聚合处理


#######################约束#####################
# 保证数据的完整性, 一致性, 有效性
# 默认约束(default)  非空约束(not null)
# sex enum("M","F","S") not null defalut "S"


###################索引#####################
# 给数据库表中的一列或者多列的值进行排序的一种结构
# 加快数据检索速度
# 占用物理空间,当对表中数据进行更新时,索引需要动态维护,减低数据维护速度
# 
#################### 普通索引(index MUL)
# 可以设置多个字段,字段值无约束
# 创建表时 create table demo 
#        (name varchar(32),
#         age tinyint unsigned, 
#         index(name), index(age));
# 已有表时 create index 索引名 on 表名(字段名);
# 查看索引 desc 表名; show index from 表名\G;
# 删除索引 drop index 索引名 on 表名;
#
#################### 唯一索引(unique UNI)
# 可以设置多个字段,字段值不允许重复,但可以为NULL
# 创建表时 create table demo 
#        (name varchar(32),
#         age tinyint unsigned, 
#         unique(name), unique(age));
# 已有表时 create unique 索引名 on 表名(字段名);
# 查看索引 desc 表名; show unique from 表名\G;
# 删除索引 drop unique 索引名 on 表名;
#
################### 主键索引(primary key PRI)
# 自增长属性(auto_increment, 配合主键一起使用)
# 只能有一个主键字段, 不允许重复,且不能为NULL
# 通常设置记录编号字段id, 能唯一锁定一个记录
# 创建表时 create table 表名
#        (id int primary key auto_increment=1000);
# 已有表添加自增长属性 alter table 表名 modify id int auto_increment;
# 已有表重新指定起始值: alter table 表名 auto_increment=2000;
# 已有表添加主键: alter table 表名 add primary key(字段)
# 删除主键
# 删除自增长属性: alter table 表名 modify id int;
# 删除主键索引: alter table 表名 drop primary key;
#
############################外键(foregin key)
# 让当前表字段的值在另一个表的范围内选择
# 主表从表字段数据类型要一致,主表被参考字段必须为主键
# 语法:
# foreign key (参考字段名)
# references 主表(被参考字段名)
# on delete 级联动作
# on uodate 级联动作
# 创建表时
# create table 表名(
# id int,
# name varchar(32),
# foreign key(参考字段名) references 主表(主键)
# on delete 级联动作
# on update 级联动作);
# 以有表添加外键
# alter table 表名 add
# foreign key (参考字段) references 主表(主键)
# on delete 级联动作
# on update 级联动作
# 删除外键
# alter table 表名 drop foreign key 外键名;
# 级联动作
# cascade    数据级联删除,更新(参考字段)
# restrict   默认,从表有相关记录,不允许主表操作
# set null   主表删除,更新,从表关联记录字段值为NULL
#
###########################表复制########################
# create table 表名 select ... from 表名 where 条件 [limit];
# 复制表结构
# create table 表名 select ... from 表名 where false;
# 复制表结构不会把原表的 键属性复制过来

################嵌套查询##################
# 将内层的查询结果作为外层的查询条件
# select ... from 表名 where 条件 (select ...);
# 把攻击值小于平均攻击值的英雄名字和攻击值显示出来
# 先找到平均值, 在找小于平均值的名字和攻击
# select name,gongji from MOSHOU.sanguo
# where
# gongji<(select avg(gongji) from MOSHOU.sanguo);
# 找出每个国家攻击力最高的英雄的名字和攻击值
# 先找到每个国家攻击最高,在根据国家和攻击找到相应的名字和攻击
# select name,gongji from sanguo
# where 
# (country,gongji) in
# (select country,max(gongji) from sanguo group by country);


##############多表连接查询##############
# 内连接: inner join
# select * from table1,table2 where 表.字段=表.字段;
# select * from table1 inner join table2 on 条件
#
# 外连接: left join  right join
# 左连接: 以左表为主显示,没有为NULL
# select * from table1 left join table2 on 条件;
# 右连接: 以右表为主显示,没有为NULL
# select * from table1 right join table2 on 条件;
# 全连接: full join
# select * from table1 full join table2 on 条件;
# 模拟全连接
# select * from table1 left join table2 on 条件 union [all]
# select * from table1 right join table2 on 条件;


##################数据导入#######################
# 把文件系统的内容导入到数据库中
# 语法
# load data infile '文件绝对路径'
# in table '表名'
# fields terminated by '分割符'
# lines terminated by '\n';
# 导入过程
# 先创建相应的表
# 把文件拷贝到数据库的默认搜索路径
#   show variables like "secure_file_priv";
# 执行数据导入语句

################数据导出#####################
# 将数据库中的记录导出到文件系统中
# 语法
# select ... from 表名
# into outfile '/var/lib/mysql-files/文件名'
# fields terminated by '分割符'
# lines terminated by '\n';

##################数据备份##################
# mysqldump -u用户名 -p 源库名 > 绝对路径.sql
# 源库名的表示方式
# --all -databases  备份所有库
# 库名               备份单个库
# -B 库1 库2         备份多个库
# 库名 表1 表2        备份指定库的多张表

##################数据恢复###############
# 命令格式(终端命令)
# mysql -u用户名 -p 目标库名 < 文件路径
# 从所有备份库中恢复某一个库(--one-database)
# mysql -u用户名 -p --one-database 目标库名 < 文件路径
# 恢复库时如果恢复到原库会将表中数据覆盖,新增表不会删除
# 数据恢复时如果恢复的库不存在,则必须创建新库

#############mysql的用户账号管理###########
# 开启mysql远程链接
# /ect/mysql/mysql.conf.d/mysqld.conf 
# #bind-address = 127.0.0.1
# /ect/init.d/mysql restart
#
# 添加授权用户
# grant 权限列表 on 库.表 to '用户名'@'%'
# identified by '密码' with geant option;
# 权限列表: all privileges select insert
# 库.表: *.* 所有库.所有表

##############存储引擎##################
# 查看所有的存储引擎: show engines;
# 创建表时指定存储引擎: ...... engine=引擎名称
# 已有表增加存储引擎:   alter table 表名 engine=innodb

###################锁################
# 解决客户端并发访问的冲突问题
# 读锁(共享锁)
# select ：加读锁之后别人不能更改表记录,但可以进行查询
# 写锁(互斥锁、排他锁)
# insert、delete、update
# 加写锁之后别人不能查、不能改
# 
# 锁粒度
# 表级锁 ：myisam
# 行级锁 ：innodb
# 
# 常用存储引擎特点
# InnoDB特点
# 共享表空间
# 表名.frm ：表结构和索引文件
# 表名.ibd ：表记录
# 支持行级锁
# 支持外键、事务操作
# 
# MyISAM特点
# 独享表空间
# 表名.frm ：表结构
# 表名.myd ：表记录 mydata
# 表名.myi ：索引文件 myindex
# 支持表级锁
# 
# 如何决定使用哪个存储引擎
# 执行查操作多的表用 MyISAM(使用InnoDB浪费资源)
# 执行写操作多的表用 InnoDB

#############MySQL调优###########
# 选择合适的存储引擎
# 读操作多 ：MyISAM
# 写操作多 ：InnoDB
# 
# 创建索引
# 在 select、where、order by常涉及到的字段建立索引
# 
################ SQL语句的优化
# where子句中不使用 != ,否则放弃索引全表扫描
# 尽量避免 NULL 值判断,否则放弃索引全表扫描
# 优化前 ：
# select number from t1 where number is null;
# 优化后 ：
# 在number列上设置默认值0,确保number列无NULL值
# select number from t1 where number=0;
# 
# 尽量避免 or 连接条件,否则放弃索引全表扫描
# 优化前 ：
# select id from t1 where id=10 or id=20 or id=30;
# 优化后：
# select id from t1 where id=10
# union all
# select id from t1 where id=20
# union all
# select id from t1 where id=30;
# 
# 模糊查询尽量避免使用前置 % ,否则全表扫描
# select name from t1 where name like "%c%";
# 
# 尽量避免使用 in 和 not in,否则全表扫描
# select id from t1 where id in(1,2,3,4);
# select id from t1 where id between 1 and 4;
# 尽量避免使用 select * ...;用具体字段代替 * ,不要返回用不到的任何字段

##############事务和事务回滚################
# 一件事从开始发生到结束的整个过程
# 确保数据一致性
# 事务和事务回滚应用
# MySQL中sql命令会自动commit到数据库
# show variables like "autocommit"
# 
# 事务应用
# 开启事务
# mysql> begin;
# mysql> ...一条或多条SQL语句
# # 此时autocommit被禁用
# 终止事务
# mysql> commit; | rollback;

#################与Python的交互###################
# 建立数据库连接(db = pymysql.connect(...))
# 建立游标对象(c = db.cursor())
# 游标方法: c.execute('sql语句')
# 提交到数据库: db.commit()
# 关闭游标对象: c.close()
# 关闭数据库对象: db.close()
# connect方法的参数
# host: 主机地址,本地localhost
# port: 端口号
# user: 用户名
# password: 密码
# database: 库
# charset: 编码方式, 推荐使用utf-8
# 数据库连接对象(db)的方法
# db.close()            关闭连接
# db.commit()           提交到数据库执行
# db.rollback()         回滚
# cursor = db.cursor()  返回游标对象,用于执行具体sql命令
# 游标方法
# cursor.execute(sql命令, [列表]) 执行sql命令
# cursor.close()                 关闭游标对象
# cursor.fetchone()              获取查询结果集的第一条数据
# cursor.fetchmany(n)            获取n条
# cursor.fetchall()              获取全部
#
##################ORM对象关系映射
# 把对象模型映射到mysql数据库: SQLAlchemy
# class User(Base):
# __tablename__ = '表名'
# id = Column(Integer, primary_key=True)
# name = Column(String(20))

