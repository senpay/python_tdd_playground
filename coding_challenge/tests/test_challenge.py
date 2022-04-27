from coding_challenge.challenge import convert_to_human_readable


def test_count_seconds_only():
    assert convert_to_human_readable(0) == ''
    assert convert_to_human_readable(1) == '1 second'
    assert convert_to_human_readable(34) == '34 seconds'
    assert convert_to_human_readable(64) == '1 minute and 4 seconds'
    assert convert_to_human_readable(124) == '2 minutes and 4 seconds'
    assert convert_to_human_readable(60) == '1 minute'
    assert convert_to_human_readable(3600) == '1 hour'
    assert convert_to_human_readable(7200 + 123) == '2 hours, 2 minutes and 3 seconds'
    assert convert_to_human_readable(3600 * 25 + 23) == '1 day, 1 hour and 23 seconds'
    assert convert_to_human_readable(3600 * 24 * 367 + 23) == '1 year, 2 days and 23 seconds'
    assert convert_to_human_readable(3600 * 24 * 365 * 2) == '2 years'

