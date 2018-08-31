from datetime import datetime
class carData():
    """储存待录入车辆资料"""
    def __init__(self,hpzl,carnumber,cllx,syxz,phone,address,location,name,ID,suoyin,edit = False,error = False,log=""):
        self.hpzl = hpzl
        self.carnumber = carnumber
        self.cllx = cllx
        self.syxz = syxz
        self.phone = phone
        self.address = address
        self.location = location
        self.name = name
        self.ID = ID        
        self.edit = edit
        self.suoyin = suoyin
        self.error = error
        self.log=log
        self.date = "2018-06-26"
        


    def show_error(self):
        
        self.error = True
        self.print_log()
    
    def show_edit(self):
        self.edit = True
        self.add_log_finish()
        self.print_log()



    def end(self):
        self.edit = True        
        self.print_log()

    def add_log_finish(self):
        self.log = "完成，%s,%s,%s,%s,%s 已录入系统。"% (datetime.now(),self.suoyin,self.carnumber,self.hpzl,self.address)  
        
    def add_error_log(self):
        self.log = "错误，%s,%s,%s,%s,%s 录入异常。"% (datetime.now(),self.suoyin,self.carnumber,self.hpzl,self.address)   
    def show_error(self):
        self.error = True
        self.add_error_log()
        self.print_log()


    def add_pass_state(self):
        self.log = "提示：%s,%s,%s,%s状态为已录入，跳过..."% (datetime.now(),self.suoyin,self.carnumber,self.hpzl)

    def print_log(self):
        print(self.log)

    def pass_state(self):
        self.edit = True
        self.add_pass_state()
        self.print_log()
