# timeapi

route | arg | method | desc |
-|-|-|-|
`/add/` | `[title, location, start, end, desc]` | POST | add an event and return it
`/dispo/` | `[]` | GET | return next 10 rdv

To enable this on a calendar:
1. go to: https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the and download the credentials.json and put it in `./timeapi/api`
2. go to `./timeapi/api`
3. launch `pip3 install --upgrade -r requirements.txt && python3 ./Object/evts.py` and click the link given to you, follow the step and give acces to your calendar
4. verify that `token.pickle` have been created
5. launch the docker using `docker-compose up -d --build`
6. test that `http://localhost:80801/test/` is working
7. request api

example:
```
{	"title": "montestapi",
	"desc": "ma description",
	"location": "114 avenue andré maginot vitry sur seine",
	"start": "2019-07-31T13:00:00",
	"end": "2019-07-31T14:00:00"
}
```
