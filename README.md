# ical-cli
Creating and adding events to `.ics` files from the command line.

### Requirements:

- Python3
- ics (`pip install ics`)

### Steps:

1. Fork and clone this repository, then navigate inside it.
2. Modify the script for your needs with some basic details (i.e. meeting location, calendar name, url following uuids)
3. Create a calendar stub for yourself:

```bash
$ python create_calendary.py my_new_calendar.ics
```

4. Add events using the tool and the following format (note: you can do this for multiple events at a time by adding another `-a`):

```bash
$ python create_calendar.py my_new_calendar.ics -a 'Lab Meeting' 'Greg will present X' '2020-04-16 13:00:00' '2020-04-16 14:00:00'
```

5. Add your calendar file to the Git tree and push it to GitHub
6. Go to your repository and get the "`raw`" URL for your calendar file
7. In your calendar app, import a calendar by URL and paste this URL
8. For all future events, just re-run the script, push the changes, and wait for them to propagate!
