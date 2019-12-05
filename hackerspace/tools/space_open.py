def getOpenNowStatus():
    from datetime import datetime
    import calendar
    import pytz
    from getConfig import get_config

    timezone = pytz.timezone(get_config('PHYSICAL_SPACE.TIMEZONE_STRING'))
    today_weekday = calendar.day_name[datetime.now(timezone).weekday()]
    now_hour = datetime.now(timezone).hour
    now_minute = datetime.now(timezone).minute
    status = 'Unknown'
    for status_change in get_config('PHYSICAL_SPACE.OPENING_HOURS')[today_weekday]:
        if now_hour >= status_change[0] and now_minute >= status_change[1]:
            status = status_change[2]
            color_indicator = status_change[3]
        else:
            break
    return '<div class="status_code_icon '+color_indicator+'"></div><div>'+status+'</div>'
