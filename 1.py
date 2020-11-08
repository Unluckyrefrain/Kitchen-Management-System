import pymysql



'''# 实例化类
x = rawMaterials("青菜",500,"斤",10)
# 访问类的属性和方法
x.pri()
a = x.trunList()
for x in a:
    print(x) 
    '''


def chushihua():
    """
    *创建用户名和密码
    登陆
    连接mysql
    开启界面
    """
    db = pymysql.connect("localhost","root","123456","test" )
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    

def chaxunRaw(i):
    """
    获取一个要查找的原材料数量
    从数据库中提取并返回
    """
    sql = "SELECT * FROM "+i
    #cursor.execute(sql)
    print(sql)



def chaxunFood():
    """
    获取一个要查找的菜品
    从数据库中提取并返回
    """

def charuRaw():
    """
    检测之前是否存在
    是 添加存货数量，平均价格
    否 插入新原材料
    """

def charuFood():
    """
    检测之前是否存在
    是 退出
    否 插入新菜
    """

def deleteRaw():
    return 0

def deleteFood():
    return 0

def diancai():
    """
    输出点菜信息到账单表中
    获取菜信息，将原材料存为字典返回
    返回后
    """


class rawMaterials:
    __name = ""
    __save = 0
    __save_unit = ""
    __val = 0

    def __init__(self, name, save, save_u, val):
        self.__name = name
        self.__save = save
        self.__save_unit = save_u
        self.__val = val
        print("__init__(self,name,save,save_u,val)")
    def pri(self):
        print("名称为:{0},进货{1}{2}，价格{3}rmb，均价{4}rmb每{2}".format(self.__name,self.__save,self.__save_unit,self.__val,self.__save/self.__val))
    def trunList(self):
        a = [self.__name,self.__save,self.__save_unit,self.__val]
        return a
class Food:
    __name = ""
    __need = ()
    __baseVal = 0
    __sellVal = 0
    __earnVal = 0
    __ifCouldCook = False
    def __init__(self,name,sval,*need):
        self.__name = name
        self.__sellVal = sval
        self.__need = need
    def pri(self):
        print(self.__name,self.__sellVal,self.__need)

if __name__ == "__main__":
    chaxunRaw("luobo")
