# by Marco Bartsch


def JSON_RESPONSE_more_results(request, template_path, queryset):
    print('LOG: JSON_RESPONSE_more_results(request,queryset)')
    from django.http import JsonResponse
    from django.template.loader import get_template

    # see if request comes from a guilde/space page, then show guilde/space events, not all events
    if request.GET.get('origin', None):
        if 'guilde/' in request.GET.get('origin', None):
            queryset = queryset.filter(
                one_guilde__str_slug=request.GET.get('origin', None)[1:])
        elif 'space/' in request.GET.get('origin', None):
            queryset = queryset.filter(
                one_space__str_slug=request.GET.get('origin', None)[1:])

    start_from = int(request.GET.get('from', None))
    upt_to = int(start_from+10)

    return JsonResponse({
        'html': get_template('components/body/'+template_path).render({
            'all_results': queryset[start_from:upt_to],
            'specific_selector': request.GET.get('specific_selector', None)
        }),
        'continue_from': upt_to,
        'more_results': True if queryset.count() > upt_to else False
    })


def DATETIME__from_date_and_time_STR(str__date, str__time):
    from hackerspace.YOUR_HACKERSPACE import HACKERSPACE_TIMEZONE_STRING
    import pytz
    from datetime import datetime
    if 'AM' in str__time or 'PM' in str__time:
        datetime_input = pytz.timezone(HACKERSPACE_TIMEZONE_STRING).localize(
            datetime.strptime(str(str__date+' '+str__time.replace(' ', '')), "%Y-%m-%d %I:%M%p"))
    else:
        datetime_input = pytz.timezone(HACKERSPACE_TIMEZONE_STRING).localize(
            datetime.strptime(str(str__date+' '+str__time.replace(' ', '')), "%Y-%m-%d %H:%M"))
    return datetime_input


def INT__UNIX_from_date_and_time_STR(str__date, str__time):
    print('LOG: INT__UNIX_from_date_and_time_STR(str__date={},str__time={})'.format(
        str__date, str__time))
    from datetime import datetime

    print('LOG: --> get datetime from string')
    datetime_input = DATETIME__from_date_and_time_STR(str__date, str__time)

    print('LOG: --> datetime to UNIX time')
    int_timestamp = round(datetime.timestamp(datetime_input))

    return int_timestamp


def INT__duration_minutes(str_duration):
    hours = int(str_duration.split(':')[0])
    minutes = int(str_duration.split(':')[1])
    return (hours*60)+minutes
