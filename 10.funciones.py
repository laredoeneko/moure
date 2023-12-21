####### Functiones #####
from datetime import datetime
log_level = True


def log(*description):
    if log_level == True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"{dt_string}  {description}")


a = 55
log("dentro del bucle", "33333", a)
