import pymysql

def get_list(sql,args):
    # 用于多行数据查询
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='yuxiaomi', db='proj_python')
    cursor = conn.cursor()
    cursor.execute(sql,args)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_one(sql,args):
    # 用于修改
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='yuxiaomi', db='proj_python')
    cursor = conn.cursor()
    cursor.execute(sql,args)
    result=cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def modify(sql,args):
    # 可用于更新删除
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='yuxiaomi', db='proj_python')
    cursor = conn.cursor()
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()

def create(sql,args):
    # 对于自增的表 返回最后一个增长的 主键id 值
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='yuxiaomi', db='proj_python')
    cursor = conn.cursor()
    cursor.execute(sql, args)
    conn.commit()
    last_row_id=cursor.lastrowid
    cursor.close()
    conn.close()
    return  last_row_id

class SQLHELPER(object):
    def __init__(self):
        # 读取配置文件
        self.connect()

    def connect(self):
        self.conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='yuxiaomi', db='dd')
        self.cursor =self.conn.cursor()

    def get_list(self,sql,args):
        self.cursor.execute(sql,args)
        result=self.cursor.fetchall()
        return result

    def get_one(self,sql,args):
        self.cursor.execute(sql,args)
        result = self.cursor.fetchone()
        return result

    def modify(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()

    def create(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()
        return self.cursor.lastrowid

    def multiple_modify(self,sql,args):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

# obj=SQLHELPER()
# obj.multiple_modify()
# obj.close()



