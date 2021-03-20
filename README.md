# Dispatching Cyber Scans
A system for dispatching cyber scans.

This system has 4 parts.

1. DB Api
2. Ingest
3. Process
4. Status

<hr/>

### DB APi

db_api is the component that communicate with the db.\
To run db_api just run the run.py file in its folder.

When you run it drop the old db and create a new one. \ 
all the request to update, insert and get from the db going \
from this component. 

run on port 8080\
Access the api with base url and /db-api/scan|scans


### Ingest
ingest is the component that the user can send new scans.\
To run ingest, just run the run.py file in its folder.

Each scan go to db_api to insert new scan and return to the user scan Id.\
The scan id is a uuid to this specific domain scan - save it to see what is going on with your scan. \
It can handle in parllel with multiprocessing and threading - need to config in the config file.\
But, in production you need to use uwsgi and Ngnix, don't use app.run with debug mode and the multiprocessing.

Run on port 5000\
Access the api with base url and /ingest/


### Process
process is the component that process the scans.\
To run process, just run the run.py file in its folder.

It run in loop and each time ask for all the new scans.\
When it gets new list of scan it update the scan status to Running.\
It try to get the url using curl command.\
When it complete the scan it send the status of the scan - Error or Complete to db api.

you can change the runtime interval in config.

The user can't access it.


### Status
status is the component that give the user option to get statuses of thier scans.\
To run status just run the run.py file.

You send the url with the scan id and get the status of this scan.\
It can be - \[Accepted, Running, Error, Complete, Not Found] 

Run on port 5001\
Access the api with base url and /status/<scan_id>
