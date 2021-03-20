# Dispatching Cyber Scans
A system for dispatching cyber scans.

This system has 4 parts.

1. DB Api
2. Ingest
3. Process
4. Status

<hr/>

### DB APi

db_api is the component that comunicate with the db.\
To run db_api just run the run.py file.

When you run it drop the old db and create new one.  
all the request to update, insert and get from the db going 
from this component. 

run on port 8080
the access to its api with base url and /db-api/scan|scans


### Ingest
ingest is the component that the user can send to it new scans.\
To run ingest, just run the run.py file in its folder.

Each scan go to db_api to insert new scan and return to the user
the UUID is the id to this specific domain scan - save it
to see what is going on with your scan. 
it can handle in parllel with multiprocessing - need to config in the config file.
but, in production you need to use uwsgi and Ngnix, don't use app.run with debug mode.

run on port 5000
the access to its api with base url and /ingest/


### Process
process is the component that process the scans.\
To run process, just run the run.py file in its folder.

it run in loop and each time ask for all the new scans.
when it gets new list of scan it update the scan status to Running.
it try to get the url using curl command.
when it complete the scan it send the status of the scan - Error or Complete to db api.

you can change the runtime interval in config.

The user can't access it.


### Status
status is the component that the user can get statuses.\
To run db_api just run the run.py file.

you send with the url with the scan id and get the status of this scan.
it can be - \[Accepted, Running, Error, Complete, Not Found] 

run on port 5001
the access to its api with base url and /status/<scan_id>
