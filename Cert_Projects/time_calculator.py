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
            converted_hours = str(int(hours) + 12)
            if converted_hours == "24":
                converted_hours = "00"
            converted_time = converted_hours + ":" + minutes
        else:
            converted_time = hours + ":" + minutes

        return converted_time

    # Check and convert from 24-hour to 12-hour system.
    else:
        if int(hours) >= 13:
            converted_hours = int(hours) - 12
            converted_time = str(converted_hours) + ":" + minutes + " PM"
        elif hours == "00":
            hours = "12"
            converted_time = hours + ":" + minutes + " PM"
        else:
            converted_time = hours + ":" + minutes + " AM"

        return converted_time


#def add_time(start, duration, starting_day=""):
