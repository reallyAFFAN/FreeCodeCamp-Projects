def add_time(start, duration, day=None):
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    
    if start_hour == 12 and period.upper() == "AM":
        start_hour = 0  
    elif start_hour != 12 and period.upper() == 'PM':
        start_hour += 12  

    
    duration_hour, duration_minute = map(int, duration.split(":"))

    
    end_minute = start_minute + duration_minute
    extra_hour = end_minute // 60
    end_minute %= 60

    
    end_hour = start_hour + duration_hour + extra_hour
    no_of_days = end_hour // 24
    end_hour %= 24

    
    display_minute = f'{end_minute:02d}'

    
    end_day = ""
    if day:
        day = day.capitalize()  
        old_index = days.index(day)
        new_index = (old_index + no_of_days) % 7  
        end_day = f", {days[new_index]}"  

    
    if end_hour == 0:
        display_hour = '12'
        display_period = 'AM'
    elif end_hour < 12:
        display_hour = str(end_hour)
        display_period = "AM"
    elif end_hour == 12:
        display_hour = "12"
        display_period = "PM"
    else:
        display_hour = str(end_hour - 12)
        display_period = "PM"

    
    if no_of_days == 1:
        days_later = " (next day)"
    elif no_of_days > 1:
        days_later = f" ({no_of_days} days later)"
    else:
        days_later = ''  

    
    result = f'{display_hour}:{display_minute} {display_period}'
    if end_day:
        result += end_day
    if days_later:
        result += days_later

    return result

print(add_time('3:30 PM', '2:12'))
