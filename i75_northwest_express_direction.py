from datetime import datetime, time
import pytz
import json

# Get the UTC Datetime object and converting to EST
datetime_utc = datetime.utcnow()
datetime_utc = datetime_utc.replace(tzinfo=pytz.UTC)
datetime_est = datetime_utc.astimezone(pytz.timezone("US/Eastern"))

# Set the day
day = datetime.weekday(datetime_est)

# Set the time
time_now = datetime_est.time()

# Set the normal operation schedule
normal_schedule = {
    0: {
        "Day": "Monday",
        "Start": "Reverse to Southbound",
        "Changes": {
            time(01, 00): "Open to Southbound",
            time(11, 30): "Reverse to Northbound",
            time(13, 00): "Open to Northbound",
            time(23, 00): "Reverse to Southbound"
        }
    },
    1: {
        "Day": "Tuesday",
        "Start": "Reverse to Southbound",
        "Changes": {
            time(00, 30): "Open to Southbound",
            time(11, 30): "Reverse to Northbound",
            time(13, 00): "Open to Northbound",
            time(23, 00): "Reverse to Southbound"
        }
    },
    2: {
        "Day": "Wednesday",
        "Start": "Reverse to Southbound",
        "Changes": {
            time(00, 30): "Open to Southbound",
            time(11, 30): "Reverse to Northbound",
            time(13, 00): "Open to Northbound",
            time(23, 00): "Reverse to Southbound"
        }
    },
    3: {
        "Day": "Thursday",
        "Start": "Reverse to Southbound",
        "Changes": {
            time(00, 30): "Open to Southbound",
            time(11, 30): "Reverse to Northbound",
            time(13, 00): "Open to Northbound",
            time(23, 00): "Reverse to Southbound"
        }
    },
    4: {
        "Day": "Friday",
        "Start": "Reverse to Southbound",
        "Changes": {
            time(00, 30): "Open to Southbound",
            time(11, 30): "Reverse to Northbound",
            time(13, 00): "Open to Northbound",
            time(23, 00): "Reverse to Southbound"
        }
    },
    5: {
        "Day": "Saturday",
        "Start": "Reverse to Southbound",
        "Changes": {
            time(00, 30): "Open to Southbound"
        }
    },
    6: {
        "Day": "Sunday",
        "Start": "Southbound",
        "Changes": {
            time(11, 30): "Reverse to Northbound",
            time(13, 00): "Open to Northbound",
            time(23, 30): "Reverse to Southbound"
        }
    },
}


def get_direction(event, context):
    print("Today is {}\n".format(normal_schedule[day]["Day"]))

    start_for_the_day = normal_schedule[day]["Start"]
    change_list = normal_schedule[day]["Changes"]

    print("It is currently {}\n".format(time_now))

    option_in_force = ""

    for k, v in sorted(change_list.iteritems()):
        if time_now > k:
            option_in_force = v
        else:
            if option_in_force == "":
                option_in_force = start_for_the_day

    print("Current Status is: {}\n".format(option_in_force))

    response = {
        "statusCode": 200,
        "body": json.dumps("Current Status is: {}".format(option_in_force))
    }

    return response

    # return "Current Status is: {}".format(option_in_force)


if __name__ == '__main__':
    get_direction("", "")