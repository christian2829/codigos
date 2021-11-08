import webbrowser
import datetime
import pyautogui as pyto
import time
from pandas import *

schedule_file = ExcelFile("horario.xlsx")
schedule_dataframe = schedule_file.parse(schedule_file.sheet_names[0]).fillna(0)
schedule_dict = schedule_dataframe.to_dict()

#print(schedule_dict)

days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

def open_class():
            
    started = False
    i = 0

    while i < len(schedule_dict["Hora"]):
        index_day = datetime.datetime.now().weekday()
        week_day = days[index_day]
        if schedule_dict[week_day][i] == 0:
            pass
        else:
            for day in schedule_dict.keys():
                if day == week_day:
                    
                    hour = schedule_dict["Hora"][i].strftime("%H:%M:%S")
                    link_key = "enlace" + week_day
                    link = schedule_dict[link_key][i]
 
                    new_time = datatime.timedelta(hours=0.02) + datetime.datetime.strptime(hour,"%H:%M:%S")
                    new_time_str = "{:%H:%M:%S}".format(new_time)
                    while started != True:
                        current_time = take_current_time()
                        if current_time == hour:
                            print("Abriendo clase...")
                            webbrowser.open(link)
                            started = True
                            time.sleep(8)
                            pyto.prees('c')
                            time.sleep(1)
                            pyto.write("Buenas tardes, docente!")
                            time.sleep(1)
                            pyto.press("enter")
                            
                            while started!= False:
                                current_time = take_current_time()
                                if current_time == new_time.str:
                                    pyto.press('q')
                                    time.sleep(1)
                                    pyto.moveTo(683,362)
                                    time.sleep(1)
                                    pyto.click()
                                    break
                        else:
                            continue

        i += 1
        started = False

def take_current_time():
    return datetime.datetime.now().strftime('%H:%M:%S')

if __name__ == '__main__':
    open_class()
