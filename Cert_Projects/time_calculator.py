def separate_hours_minutes(hours_minutes):
    """Take string 'hours_minutes' in hours:minutes format and returns 'hours' and 'minutes' separately."""

    # Variables to be returned when processed.
    hours = ""
    minutes = ""

    # Separate hours.
    index = 0
    for char in hours_minutes:
        if char == ":":
            index += 1
            break
        else:
            hours += char
            index += 1

    # Separate minutes.
    for char in hours_minutes[index:]:
        if index == len(hours_minutes):
            break
        # Following if-clause only of use when function is used in 'convert_time_system()' function.
        if char.lower() == "a" or char.lower() == "p" or char.lower() == "m":
            index += 1
            break
        else:
            minutes += char
            index += 1

    return hours, minutes


def convert_time_systems(time):
    """Convert string 'time' between 12-hour and 24-hour system."""

    hours, minutes = separate_hours_minutes(time)

    # Check and convert from 12-hour to 24-hour system.
    if "m" in time.lower():
        if "p" in time.lower():
            if hours == "12":
                converted_hours = "12"
            else:
                converted_hours = str(int(hours) + 12)
            converted_time = converted_hours + ":" + minutes
        else:
            if hours == "12":
                hours = "00"
            converted_time = hours + ":" + minutes

        return converted_time

    # Check and convert from 24-hour to 12-hour system.
    else:
        if int(hours) >= 12:
            if hours == "12":
                converted_time = hours + ":" + minutes + " PM"
            else:
                converted_hours = int(hours) - 12
                converted_time = str(converted_hours) + ":" + minutes + " PM"
        elif hours == "00" or hours == "0":
            converted_time = "12" + ":" + minutes + " AM"
        else:
            converted_time = hours + ":" + minutes + " AM"

        return converted_time


def convert_hours_to_days(hours):
    """Take string 'hours' and return 'days' and 'hours_remain'."""

    days = int(hours) // 24
    hours_remain = int(hours) % 24

    return str(days), str(hours_remain)


def add_time(start, duration, starting_day=""):

    # Convert argument 'start' to 24h system and assign hours and minutes to separate variables.
    start_time_24h = convert_time_systems(start)
    start_hours_24h, start_minutes = separate_hours_minutes(start_time_24h)

    # Assign hours and minutes from argument 'duration' to separate variables.
    duration_hours, duration_minutes = separate_hours_minutes(duration)

    # Add hours and minutes from 'start' and 'duration' arguments.
    sum_hours = str(int(start_hours_24h) + int(duration_hours))
    sum_minutes = str(int(start_minutes) + int(duration_minutes))
    # Switch to next hour at 60 minutes.
    if int(sum_minutes) >= 60:
        sum_minutes = str(int(sum_minutes) - 60)
        # if-clause to ensure two-digit format for 'sum_minutes'.
        if len(sum_minutes) == 1:
            sum_minutes = "0" + sum_minutes
        sum_hours = str(int(sum_hours) + 1)

    # Calculate number of days passed and time of day for final return value.
    days_passed, hours_remain = convert_hours_to_days(sum_hours)
    new_time_24h = hours_remain + ":" + sum_minutes
    output_time = convert_time_systems(new_time_24h)

    # Outputs weekday for final return value if optional argument is assigned in function call.
    if starting_day:
        weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
        output_day = ""
        day_count = int(days_passed)
        day = starting_day.lower()
        day_index = weekdays.index(day)
        day_index_counter = day_index + day_count

        if day_count == 0:
            output_day = weekdays[day_index].title()
        else:
            if day_index_counter <= 6:
                output_day = weekdays[day_index_counter].title()

    # Reassign 'days_passed' variable for final return value.
    if days_passed == "0":
        pass
    elif days_passed == "1":
        days_passed = "(next day)"
    else:
        days_passed = f"({days_passed} days later)"



    # TEST PRINT STATEMENTS!!!
    print(output_time)
    if starting_day:
        print(output_day)
    if days_passed != "0":
        print(days_passed)
    print("")


# Test function calls
add_time('3:00 PM', '3:10')  # Returns: 6:10 PM
add_time('11:30 AM', '2:32', 'Monday')  # Returns: 2:02 PM, Monday
add_time('11:43 AM', '00:20')  # Returns: 12:03 PM
add_time('10:10 PM', '3:30')  # Returns: 1:40 AM (next day)
add_time('11:43 PM', '24:20', 'tueSday')  # Returns: 12:03 AM, Thursday (2 days later)
add_time('6:30 PM', '205:12')  # Returns: 7:42 AM (9 days later)
add_time('8:16 PM', '466:02', 'tuesday') # Returns: 6:18 AM, Monday (20 days later)