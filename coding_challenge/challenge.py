SECONDS_IN_SECOND = 1
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR
SECONDS_IN_YEAR = 365 * SECONDS_IN_DAY

TIME_UNITS = {
    'year' : SECONDS_IN_YEAR,
    'day' : SECONDS_IN_DAY,
    'hour' : SECONDS_IN_HOUR,
    'minute' : SECONDS_IN_MINUTE,
    'second' : SECONDS_IN_SECOND,
}

TIME_UNIT_LIST = ['year', 'day', 'hour', 'minute', 'second']

def pluralize(time, time_unit):
    if time > 1:
        return f'{time_unit}s'
    else:
        return time_unit

def count_time_units(seconds, time_unit_list, time_units):
    if not time_unit_list:
        return []
    current_time_unit = time_unit_list[0]
    return ([count_time_unit(seconds, time_units[current_time_unit], current_time_unit)] +
            count_time_units(seconds % time_units[current_time_unit], time_unit_list[1:], time_units))
    

def count_time_unit(seconds, seconds_in_time_unit, time_unit_name):
    time_unit = seconds // seconds_in_time_unit
    if time_unit:
        return f'{time_unit} {pluralize(time_unit, time_unit_name)}'
    else:
        return ''

def combine_last_two_with_and(str_list):
    if len(str_list) < 2:
        return str_list
    else:
        return str_list[:-2] + [f'{str_list[-2]} and {str_list[-1]}']

def filter_empty_elements(ls):
    return [x for x in ls if x]

def convert_to_human_readable(seconds):
    result = combine_last_two_with_and(
        filter_empty_elements(
            count_time_units(seconds, TIME_UNIT_LIST, TIME_UNITS)
        )
    )
    return ', '.join(result)
