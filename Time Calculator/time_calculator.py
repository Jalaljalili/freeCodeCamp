def add_time(start_time, duration, start_day=None):
  # Parse start_time
  start_time, am_pm = start_time.split()
  start_hour, start_minute = map(int, start_time.split(':'))
  
  # Parse duration
  duration_hour, duration_minute = map(int, duration.split(':'))
  
  # Convert start_time to 24-hour format
  if am_pm == 'PM':
      start_hour += 12
  
  # Calculate total minutes
  total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
  
  # Calculate new time
  new_hour = total_minutes // 60 % 24
  new_minute = total_minutes % 60
  
  # Determine AM or PM
  new_am_pm = 'AM' if new_hour < 12 else 'PM'
  
  # Adjust for 12-hour clock
  new_hour = new_hour % 12
  new_hour = 12 if new_hour == 0 else new_hour
  
  # Determine the number of days later
  days_later = total_minutes // (24 * 60)
  
  # Determine the day of the week if start_day is provided
  if start_day:
      start_day = start_day.capitalize()
      days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      start_index = days_of_week.index(start_day)
      new_day_index = (start_index + days_later) % 7
      new_day = days_of_week[new_day_index]
      result = f"{new_hour}:{new_minute:02d} {new_am_pm}, {new_day}"
  else:
      result = f"{new_hour}:{new_minute:02d} {new_am_pm}"
  
  # Append (next day) or (n days later) to the result if needed
  if days_later == 1:
      result += " (next day)"
  elif days_later > 1:
      result += f" ({days_later} days later)"
  
  return result
