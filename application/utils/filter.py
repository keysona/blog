def format_datetime(datetime):
    return "%s年%s月%s日 %s:%s" % (datetime.year, datetime.month, datetime.day,
                                datetime.hour, datetime.second)
