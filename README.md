# redis-kafka-most-recent

Service that stores word entries for a user and fetches the most recent entries. 

Entries are stored in MySQL and cached in Redis.

When fetching entries Redis will be used. If Redis is empty then MySQL will be used. 
If data is found in MySQL it will get backfilled into Redis for the next fetch. 


# start server

First, bring up the dependencies:
`docker-compose up`

Then, run the server:
`FLASK_APP=./src/server.py flask run`

# send requests

Scripts are provided to post and get entries. 

`./scripts/create.sh`
`./scripts/recents.sh`


# todo
- document graphite
