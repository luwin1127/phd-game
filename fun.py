
def add_date(click_num, yr, mh):
    mh = mh + click_num
    if mh > 12:
        mh = 1
        yr += 1
    return yr, mh