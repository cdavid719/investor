import datetime

def actions(fname, lname, text):
    if(text=="username"):
        with open("log.txt", "a") as log:
            log.write('\n' + str(datetime.datetime.now()))
            log.write(f"\nUser {fname} {lname} has just entered  username.")
            log.close
    else:
        with open("log.txt", "a") as log:
            log.write('\n' + str(datetime.datetime.now()))
            log.write(f"\nUser {fname} {lname} has just entered  password.")
            log.close