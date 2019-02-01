README.md

VisitTampere API:n käyttö esimerkkinä API-ohjelmoinnin prosessista ja periaatteista Python-kielellä.

Testaillaan rajapintaa - [vuorovaikutteinen dokumentaatio](https://visittampere.fi/api-docs/) on näppärä! Käytössä [Swagger](https://swagger.io/).

Seuraavaksi käyttöön [Postman](https://www.getpostman.com/).

[Requests-kirjasto](https://tutorialedge.net/python/python-http-requests-tutorial/) tekee HTTP-pyyntöjen Python-ohjelmoinnista helppoa.

Pohditaan yhdessä mitä ja miksi seuraavissa askeleissa tapahtuu:

Ympäristöasiat kuntoon

	python3 -m venv VENV
	
	source VENV/bin/activate

Packages

    pip install -r requirements.txt

Alternative to Jupyter

    ipython

python vs. run

    run sample_events.py
