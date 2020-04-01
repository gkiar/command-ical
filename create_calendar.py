#!/usr/bin/env python

from ics import Calendar, Event


c = Calendar()
e = Event()

e.name = "My cool event"
e.begin = '2020-04-02 09:00:00'

c.events.add(e)

print(c.events)

with open('test-calendar.ics', 'w') as my_file:
    my_file.writelines(c)
