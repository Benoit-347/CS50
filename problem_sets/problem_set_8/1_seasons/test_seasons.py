from datetime import date
import seasons

def test_str_to_date():
    assert seasons.str_to_date('1991-01-01') == date(1991, 1, 1)
def test_get_mins():
    date_1 = date(1999, 1, 1)
    date_2 = date(2000, 1, 1)
    assert seasons.get_mins(date_2, date_1) == 525600
def test_get_prefix():
    assert seasons.get_prefix(999) == 'nine hundred ninety-nine'
    assert seasons.get_prefix(19) == 'nineteen'

def test_conv_num_to_str():
    assert seasons.conv_num_to_str(18349920) == 'Eighteen million, three hundred forty-nine thousand, nine hundred twenty'
