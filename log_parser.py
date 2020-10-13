""" log parser
    Accepts a filename on the command line. The file is a Linux-like log file
    from a system you are debugging. Mixed in among the various statements are
    messages indicating the state of the device. They look like this:
        Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON
    The device state message has many possible values, but this program cares
    about only three: ON, OFF, and ERR.

    Your program will parse the given log file and print out a report giving
    how long the device was ON and the timestamp of any ERR conditions.
"""

from datetime import datetime

input_log = [
    "Jul 10 10:00:51:490 [139681125603136] dut: Device State: ERR",
    "Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON",
    "Aug 07 09:11:51:490 [139681125603136] dut: Device State: OFF",
    "Aug 12 10:00:51:490 [139681125603136] dut: Device State: ERR",
    "Aug 15 10:00:51:490 [139681125603136] dut: Device State: INFO",
    "Aug 15 10:00:51:490 [139681125603136] dut: Device State: ON",
    "Aug 20 09:11:51:490 [139681125603136] dut: Device State: OFF",
]

def analyze_log(input_log):
    device_is_on = False
    device_started_at = None
    for line in input_log:
        tokens = line.split(':')
        error_code = __get_error_code(tokens)
        timestamp = __get_timestamp(tokens)
        if error_code == "ERR":
            print(f"Error condition at {timestamp}")
        if error_code == "ON" and not device_is_on:
            device_started_at = timestamp
            device_is_on = True
        if error_code == "OFF" and device_is_on:
            print(f'Device on from {device_started_at} to {timestamp}')
            device_is_on = False


def __get_error_code(tokens):
    return tokens[-1].strip()

def __get_timestamp(tokens):
    return datetime.strptime(''.join(tokens[:3]), '%b %d %H%M%S')


analyze_log(input_log)   

