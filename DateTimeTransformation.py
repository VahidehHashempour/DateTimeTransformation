from datetime import datetime

# Variable now stores the current dateTime
now = datetime.now()

# Variable date stores date value in variable now converted to date String format 1
# New feature name of day in the week added
date = now.strftime("%d/%m/%Y %A")

print('Date String:', date)

# Variable date stores date value in variable now converted to date String format 2
# New feature name of day in the week added
date = now.strftime("%d-%m-%Y %A")

print('Date String:', date)

# Variable time stores time value in variable now converted to time String format 1
time = now.strftime("%H:%M:%S")

print('Time String:', time)

# Variable time stores time value in variable now converted to time String format 2
time = now.strftime("%I:%M:%S %p")

print('Time String:', time)
