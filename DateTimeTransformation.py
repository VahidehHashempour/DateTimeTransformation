from datetime import datetime

# current dateTime
now = datetime.now()

# convert to date String
date = now.strftime("%d/%m/%Y %A")
print('Date String:', date)

date = now.strftime("%d-%m-%Y %A")
print('Date String:', date)

# convert to time String
time = now.strftime("%H:%M:%S")
print('Time String:', time)

time = now.strftime("%I:%M:%S %p")
print('Time String:', time)
