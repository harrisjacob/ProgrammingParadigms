# Climate Database Webservice
This project was an introduction to CherryPy and RESTful webservices. This is only a MVP.

This API is to be used to help give the user information about potential locations he/she either wants to visit, or is interested in.
The user will be able to search locations based on temperature or dryness based on month, or even with what their ideal temperature would be.
Additionally, the user can add or delete entries if they so choose to do so.
To use the unit tests, simply type "python3 test_api.py"
This server must be started prior to starting the tests (see client update for instructions)

# Web Service Update
Our service runs on port 48. Our webservice could be used by customers in lots of different ways. We could use it so that travellers could look up information about the cities they are travelling too so they could better plan. It would also allow people to put new weather information so that the database stays up to date with the latest weather trends.

#Client Update
A client was implemented and can be found at:
http://student04.cse.nd.edu/jharri18/climate/
This will allow you to query the database using a month and city.
There are links to the add city and update city pages at the bottom.
To start the server simply run 'python3 main.py'

Currently the specified URL cannot be reached from networks outside of the University of Notre Dame.  In future versions of this project, the server will be hosted elsewhere. In the meantime, please contact the owner for questions.
