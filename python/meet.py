import webbrowser
import datetime
import pyautogui as pyto
import time
from pandas import *

schedule_file = ExcelFile("horario.xlsx")
schedule_dataframe = schedule_file.parse(schedule_file.sheet_names[0]).fillna(0)
schedule_dict = schedule_dataframe.to_dict()

days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

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
                        link_key = "Enlace" + week_day
                        link = schedule_dict[link_key][i]
                                    
                        new_time = datetime.timedelta(hours=0.02) + datetime.datetime.strptime(hour, "%H:%M:%S")
                        new_time_str = "{:%H:%M:%S}".format(new_time)
                        while started != True:
                            current_time = take_current_time()
                            if current_time == hour:
                                print("Abriendo clase...")
                                webbrowser.open(link)
                                started = True
                                time.sleep(5)
                                pyto.hotkey('ctrlleft', 'd')
                                pyto.hotkey('ctrlleft', 'e')
                                time.sleep(1)
                                pyto.moveTo('977,534')
                                pyto.click()
                                time.sleep(3)
                                pyto.hotkey('ctrlleft', 'altleft', 'c')
                                time.sleep(2)
                                pyto.write("Buenas tardes, profe")
                                time.sleep(1)
                                pyto.press("enter")

                                while started != False:
                                    current_time = take_current_time()
                                    if current_time == new_time_str:
                                        pyto.moveTo('787','730')
                                        pyto.click()
                                        time.sleep(1)
                                        break
                                    else:
                                        continue
                                        
                                        
                i += 1
                started = False

def take_current_time():
    return datetime.datetime.now().strftime('%H:%M:%S')

if __name__ == '__main__':
    open_class()
