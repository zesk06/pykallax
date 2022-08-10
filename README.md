# pykallax

a python CLI to interact with [kallax.io](https://kallax.io/) [API](https://kallax.io/swagger/index.html)

```bash
# in a venv
pip install - r requirements.txt
python3 pykallax.py --help
# add your token API to .env (see .env.example)
# and run 
python3 pykallax.py
```

The output (for now) is something like:

```bash
{'identifier': 'L00X8', 'title': 'Arkham Horror: The Card Game – The Path to Carcosa: Campaign Expansion'}
{'identifier': 'BZE42', 'title': 'Arkham Horror: Dunwich Horror Expansion'}
{'identifier': 'L3635', 'title': 'Time of Legends: Joan of Arc'}
{'identifier': 'P1OD0', 'title': 'Frosthaven'}
{'identifier': 'HXESU', 'title': 'Red Rising'}
```

