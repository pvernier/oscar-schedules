from oscar_schedules.schedule import Schedule


def oscar2schedule(row):

    month_from = int(row["MONTH_SINCE_NU"])
    month_to = int(row["MONTH_TILL_NU"])
    week_from = int(row["WEEKDAY_SINCE_NU"])
    week_to = int(row["WEEKDAY_TILL_NU"])
    hour_from = int(row["HOUR_SINCE_NU"])
    hour_to = int(row["HOUR_TILL_NU"])
    min_from = int(row["MINUTE_SINCE_NU"])
    min_to = int(row["MINUTE_TILL_NU"])
    interval = int(row["TEMP_REP_INTERVAL_NU"])
    if interval == 0:
        raise ValueError("temporal reporting interval cannot be 0")

    international = int(row["INTERNATIONAL_EXCHANGE_YN"]) == 1
    status = row["OPERATING_STATUS_DECLARED_WMO306"]

    s = Schedule(
        month_from,
        week_from,
        hour_from,
        min_from,
        month_to,
        week_to,
        hour_to,
        min_to,
        interval,
        international,
        status,
    )

    return s
