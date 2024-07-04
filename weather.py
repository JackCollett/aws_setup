

def report_weather(temp, rep):
    return rep(temp)

def as_sun_lover(temp):
    if temp >= 25:
        return 'great'
    else:
        return 'not great'
    
def as_snow_lover(temp):
    if temp <= 0:
        return 'great'
    else:
        return 'not great'
        
report_weather(24, as_sun_lover)