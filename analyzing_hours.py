def meeting_hours(meeting):
    meeting_list = meeting.split("-")
    meetings_begin_list = meeting_list[0].split(":")
    meetings_ends_list = meeting_list[1].split(":")

    if int(meetings_begin_list[0]) < 8:
        return False

    elif int(meetings_begin_list[0]) < int(meetings_ends_list[0]):
        calculate_hours = int(meetings_ends_list[0]) - int(meetings_begin_list[0])
        return int(calculate_hours)
    
    else:
        return 0
       
    
def meeting_minutes(meeting):
    meeting_list = meeting.split("-")
    meetings_ends_list = meeting_list[1].split(":")
    meetings_begin_list = meeting_list[0].split(":")

    calculate_minutes = int(meetings_ends_list[1]) - int(meetings_begin_list[1])
    return int(calculate_minutes)

def calculate_hours_minutes(hours=0, minutes=0):
    if minutes < 0:
        hours -= 1
        minutes = 60 + minutes
      
    total_hours = hours + minutes / 60
    return total_hours
    