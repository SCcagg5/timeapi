# timeapi

route | arg | method | desc |
-|-|-|-|
`/add/` | `[title, location, start, end, desc]` | POST | add an event and return it
`/dispo/` | `[]` | GET | return next 10 rdv

To enable this on a calendar:
0. go to: https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the and download the `credentials.json` and put it in `./timeapi/api`
1. rename it `credentials_YOURMAIL.json`
2. go to `./timeapi/api`
3. launch `pip3 install --upgrade -r requirements.txt && python3 ./Object/evts.py YOURMAIL` and click the link given to you, follow the step and give acces to your calendar
4. verify that `token_YOURMAIL.pickle` have been created
5. launch the docker using `docker-compose up -d --build`
6. test that `http://localhost:80801/test/` is working
7. request api


To add multiple users:
0. get all the `credentials.json`
1. rename them `credentials_MAIL_N.json`
3. launch `python3 ./Object/evts.py MAIL_1 MAIL_2 MAIL_3 ... MAIL_N`

example:
```
{	"title": "montestapi",
	"desc": "ma description",
	"location": "114 avenue andré maginot vitry sur seine",
	"start": "2019-07-31T13:00:00",
	"end": "2019-07-31T14:00:00",
	"mail": "test@test.fr"
}
```
