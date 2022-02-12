import datetime
import winsound

def set_alarm(timing):
    date_time=str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    print(date_time)
    hour=int(date_time[11:13])
    minutes=int(date_time[14:16])
    print(hour)
    print(minutes)
    print('Alarm set at '+timing)
    while True:
        if hour==datetime.datetime.now().hour:
            if minutes==datetime.datetime.now().minute:
                print('Alarm clock running')
                winsound.PlaySound('win',winsound.SND_LOOP)
        elif hour<datetime.datetime.now().minute:
            break






