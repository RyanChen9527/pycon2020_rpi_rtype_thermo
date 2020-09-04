import os 
import time
import subprocess

interface = "wlan0"
wifi_name_list=['wsmc-office','WSMC-602','wsmc-pi','wsmc-pi2','wsmc-pi3','WSMC-ARM']
#step 1======ping======================
def check_ping():
    hostname = "www.google.com"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    print(pingstatus)
    return pingstatus
#step 2======find_the_optimal_cell=====
def get_quality(cell):
    quality = matching_line(cell,"Quality=").split()[0].split('/') #63/70  Signal level=-47 dBm =>[63]/[70]
    name=matching_line(cell,"ESSID:").split()[0].split('"') # "wsmc-office" => []"[wsmc-office]"[]
    return (int(round(float(quality[0]) / float(quality[1]) * 100)),name[1])  
    
def matching_line(lines, keyword):
    #Returns the first matching line in a list of lines. See match()
    for line in lines:
        matching=match(line,keyword)
        if matching!=None:
            return matching
    return None

def match(line,keyword):
    """If the first part of line (modulo blanks) matches keyword,
    returns the end of that line. Otherwise returns None"""
    line=line.lstrip()
    length=len(keyword)
    if line[:length] == keyword:
        #print(line[length:],"=====@@@%#%######")
        return line[length:]
    else:
        return None
        
def find_wifi():
    cells=[[]]
    parsed_cells=[]
    print("comeeeee!!!!to find~~~")
    proc = subprocess.Popen(["sudo" ,"iwlist", interface, "scan"],stdout=subprocess.PIPE, universal_newlines=True)  #add sudo in head 
    #proc.wait()
    out, err = proc.communicate()
    #print(out)                          #catch all data
    for line in out.split("\n"): # 一列一列吐出來
        #print(line) 
        cell_line = match(line,"Cell ")#找出有cell開頭那一列 代表一個段落的開頭
        if cell_line != None:
            #print (cell_line,"sssssss")
            cells.append([])#如果找到 list放一個空的給下一個用
            line = cell_line[-27:]#把cell開頭那列開頭的cell去除  只留下 address: 86:C7:EA:C1:FA:4B(從最後倒數27個字到最後)
            print(line,"@@@@@@============")#只會有mac print出來
        cells[-1].append(line.rstrip())#把讀取的列存進去(在斷行之前的列) 一列一列存進去 存到-1的list裡面(最尾的list[]) 
    cells=cells[1:] #去除第一個(存的是scan complate)
    print(cells[0])
    for cell in cells:
        # get_quality now returns an integer
        parsed_cells.append((get_quality(cell)))
        print (get_quality(cell))
    parsed_cells.sort(reverse=True) #sort
    for elemt in parsed_cells:
        if elemt[1] in wifi_name_list:  #check wifibase exit in record
            change_wifi(elemt[1])   #change
            time.sleep(10)
            if check_ping()=="Network Active":
                break  #jump

#step 3======change======================
def change_wifi(wififile_name):
	print('change=>>>>>>>>>>>>>>>',wififile_name)
	print('begin change by shhhhhhhh')
	cmd='sudo /etc/wpa_supplicant/switchwifi.sh '+wififile_name+'.conf'
	os.system(cmd)
	time.sleep(3)
	print('restart dhcpd')
	cmd='sudo systemctl restart dhcpcd'
	os.system(cmd)
     
if __name__ == "__main__":
    while True:
        if check_ping()="Network Error":
            find_wifi()
        time.sleep(60)
