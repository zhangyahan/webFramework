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
# 普通索引(index MUL)
# 可以设置多个字段,字段值无约束
# 创建表时 create table demo 
#        (name varchar(32),
#         age tinyint unsigned, 
#         index(name), index(age));
# 已有表时 create index 索引名 on 表名(字段名);
# 查看索引 desc 表名; show index from 表名\G;
# 删除索引 drop index 索引名 on 表名;
#
# 唯一索引(unique UNI)
# 可以设置多个字段,字段值不允许重复,但可以为NULL
# 创建表时 create table demo 
#        (name varchar(32),
#         age tinyint unsigned, 
#         unique(name), unique(age));
# 已有表时 create unique 索引名 on 表名(字段名);
# 查看索引 desc 表名; show unique from 表名\G;
# 删除索引 drop unique 索引名 on 表名;
#
# 主键索引(primary key PRI)
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
# 外键索引
# 从表和主表的数据类型必须一直, 关联主表的键必须时主键索引
# 创建表时
# create table 表名
# (id int ,
# grade int
# foreign key (自己的键) references student (主表主键)
# )
# 已有表时
# alter table 表名
# add constraint 自定义外键名 
# foreign key (id) references student (id)
# on update 级联动作
# on delete 级联动作

# 如果不指定CONSTRAINT symbol，MYSQL会自动生成一个名字。
# ON DELETE、ON UPDATE表示事件触发限制，可设参数：
# RESTRICT（限制外表中的外键改动，默认值）
# CASCADE（跟随外键改动）
# SET NULL（设空值）
# SET DEFAULT（设默认值）
# NO ACTION（无动作，默认的）










