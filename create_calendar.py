#!/usr/bin/env python

from argparse import ArgumentParser
from ics import Calendar, Event
from ics.grammar.parse import ContentLine
import os.path as op


example_e = ['Lab Meeting', 'Tristan will present X',
                 '2020-04-16 13:00:00', '2020-04-16 14:00:00']
example_e_str = str(example_e).strip('[]').replace(',','')

def createEvent(name, description, start, end):
    e = Event()

    e.name = name
    e.description = description
    e.begin = start
    e.end = end

    return e


def loadCalendar(ical):
    if not op.exists(ical):
        raise FileNotFoundError()
    else:
        with open(ical, 'r') as fhandle:
            c = Calendar(fhandle.read())
        return c


def updateCalendar(cal_obj, new_events):
    for new_e in new_events:
        tmp_e = createEvent(*new_e)

        cal_obj.events.add(tmp_e)

    return cal_obj


def main():
    parser = ArgumentParser(__file__)
    parser.add_argument("calendar_file")
    parser.add_argument("--add-event", "-a", nargs=4, action="append",
                        help="Event details to be added. Four values expected, "
                             "space separated: name, description, start, and "
                             "end. Example:\n  {0}.".format(example_e_str) +\
                             "\nYou can add multiple events by using the flag "
                             "repeatedly.")

    results = parser.parse_args()
    ical = results.calendar_file
    new_events = results.add_event

    try:
        cal_obj = loadCalendar(ical)
    except FileNotFoundError as e:
        cal_obj = Calendar()
        cal_obj.scale = 'gregorian'
        cal_obj.extra.append(ContentLine('X-WR-TIMEZONE', {},
                                         'America/Toronto'))
        cal_obj.extra.append(ContentLine('X-WR-CALNAME', {},
                                         'slash /bin'))

    if new_events is not None:
        cal_obj = updateCalendar(cal_obj, new_events)

    with open(ical, 'w') as fhandle:
        fhandle.write(str(cal_obj))


if __name__ == "__main__":
    main()

