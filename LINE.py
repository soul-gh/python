import sys
import datetime
class Payment:
    start_day
    work_num = 0
    employee_num =0
    staff_payment_list = {}

    def __init__(self, start_day, work_num, employee_num):
        self.start_day = start_day
        self.work_num = work_num
        self.employee_num = employee_num
   
    def submit(self, staff_id, can_work_day, work_list):
        if(not self.check_work_possible_num(can_work_day) or not self.check_work_possible_num(len(work_list))):
            print('wrong format')
            return
        if(can_work_day != len(work_list)*2 ):
            print('wrong format')
            return
        new_work_list = []
        for i in range(0,len(work_list),2):
            if(not self.check_work_possible_num(work_list[i]) or not self.verify_date(work_list[i]) or !self.verify_time(work_list[i+1])):
                print('wrong format')
                return
            else:
                new_work_list.append(work_list[i]+ '' + work_list[i+1])
        if(len(new_work_list)):
            self.staff_payment_list[staff_id] = new_work_list 
            print('accepted')
        return   
    
    def check(self,staff_id):
        if(self.staff_payment_list[staff_id]):
            print(len(staff_payment_list[staff_id]))
        for i  in range(staff_payment_list[staff_id]):
            print(staff_payment_list[staff_id][i].split(' ')[0])
    def calculate(self, staff_id):
        if(self.staff_payment_list[staff_id]):
            print(self.calculate_money(staff_id))
    def cancel(self, staff_id, cancel_date):



    def check_work_possible_num(S):
        if(S >= 1 and S <= 10):
            return True;
    return False;

    def verify_date(datetime_str):
        try:        
    	    datetime.datetime.strptime(datetime_str, '%m/%d')        
    	    return True    
        except ValueError:        
    	    return False

    def verify_time(time_str):
        try:
            if '-' in time_str:
                time_list = time_str.split('-')
            else:
                time_list = time_str.split('')
            print(time_list)
            for i in range(len(time_list)):
                datetime.datetime.strptime(time_list[i],'%H:%M')
            return True
        except ValueError:
            return False

    def check_date_after(self,check_date):
        check_date = datetime.datetime.strptime(check_date,'%m/%d').date()
        if(check_date >= self.start_day):
            return True
        else:
            return False   
    
    def calculate_money(staff_id):
        cur_staff = self.staff_payment_list[staff_id])
        all_time = 0
        for i in range(len(cur_staff)):
            time = cur_staff[i].split(" ")[1]
            start_time = time.split("-")[0]
            end_time = time.split("-")[1]
            start_time = datetime.datetime.strptime(start_time,'%H:%M').date()
            end_time = datetime.datetime.strptime(end_time,'%H:%M').date()
        

def split1(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')




def main(lines):
    split1(lines)

    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
