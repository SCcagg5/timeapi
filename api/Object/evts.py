from __future__ import print_function
import datetime
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/calendar']
class evts:
    def getcred(mail, verbose = False):
        creds = None
        if os.path.exists('token_'+mail+'.pickle'):
            with open('token_'+mail+'.pickle', 'rb') as token:
                creds = pickle.load(token)
                print("token for " + mail + " is ok")
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                if verbose is True:
                    print("token for " + mail + " as been updated")
            else:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials_'+mail+'.json', SCOPES)
                except:
                    if verbose is True:
                        print("file credentials_"+mail+".json doesn't exist")
                    return [False, "file credentials_"+mail+".json doesn't exist", 404]
                creds = flow.run_local_server(port=0)
            with open('token_'+mail+'.pickle', 'wb') as token:
                pickle.dump(creds, token)
                if verbose is True:
                    print("token for " + mail + " is ok")
        return [True, creds, None]

    def disp(creds):
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId='primary', timeMin=now,maxResults=10, singleEvents=True,orderBy='startTime').execute()
        events = events_result.get('items', [])
        return [True, {"events": events}, 200]

    def add(title, desc, location, start, end, creds):
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        event = {
          'summary': title,
          'location': location,
          'description': desc,
          'start': {
            'dateTime': start,
            'timeZone': 'America/Los_Angeles',
          },
          'end': {
            'dateTime': end,
            'timeZone': 'America/Los_Angeles',
          },
          'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
          ],
          'attendees': [],
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 24 * 60},
              {'method': 'popup', 'minutes': 10},
            ],
          },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        return [True, {"event": event}, 200]

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        evts.getcred(arg, True)
