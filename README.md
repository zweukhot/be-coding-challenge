# be-coding-challenge

### Expectations
- We do not expect you to completely finish the challenge. We ask that candidates spend 4 hours or more working through the challenge. With that we understand that everyones schedule and availability is different so we ask that you provide a reasonable estimate of your time commitment so we can take it into account when evaluating your submission.
- We expect you to leverage creative license where it makes sense. If you'd like to change the project structure, pull in libraries, or make assumptions about the requirements we openly encourage you to do so. All that we ask is that you are prepared to talk about your choices in future interviews. 

### Challenge
For this challenge you will be implementing a family tree API.

The API should be capable of keeping track of people and the connections between them.

While you have full control to model the entities as you see fit you should keep the following guidelines in mind.

Details about a person and their relationships should be editable. At a minimum you should use the following traits to describe a person: 
- First name
- Last name
- Phone number
- Email address
- Address
- Birth date

When thinking about relations between people the API should be able to provide the following information
- For a given person list all of their siblings
- For a given person list all of their parents
- For a given person list all their children
- For a given person list all of their grandparents
- For a given person list all of their cousins

### Getting started

##### Running the service in a virtual environment
If you are using python 3.7 you will need to run
```bash
pipenv run pip install pip==18.0
```

To install dependencies you will need to run
```bash
pipenv install
```

Once dependencies are installed you can run the service with
```bash
pipenv run python manage.py
```
or
```bash
pipenv shell
python server.py
```

### Assumptions
During the course of this exercise I have tried to take into account the following edge cases:
- A family tree is not only the bloddlines, but also divorces and remarriages. For this, N parents are allowed per child.
- Time travel is forbidden, so a person cannot be it's own father. I have enforced this in the models
- People are not their own sibling, nor their own cousin, so I have filtered out the person we are asking for
- I am assuming this API to be used by another system that will leverage the id's of the users instead of their name, but this is easily changeable for a json data payload format with at least the first name, last name and date of birth. To this end I have included a "get user by name" kind of function that will return this and other information. This choice is based on complaints from web developers using react that don't want to have to change their urls in their components when user names are updated.
- This system is used for family trees, but the family slices themselves are fairly small. I have chosen to work on smaller chunks of data on the python side rather than joining multiple times tables than can have very large amounts of data. I am aware that there are scenarios that can break this, and a performance/characterization study of the system under real loads would be necessary to find the corret balance.

### Technical decisions
I have divided the system in the following parts:
- The blueprint itself: this is mostly an argument parsing and early error management. This simplifies changes like using names instead of id's by simply swapping the arguments and using the request payload or even new paths, and then using "get_person" to find the id. The rest of the system can work as before
- The resources module: this is the intermediate layer that knows enough about the general disposition of the objects. It can combine multiple calls to the datamodel, retrieve the information it needs, filter it and prepare it in a dictionary for the jsonify call on the blueprint
- The datamodels: I have tried to keep the nitty gritty details of the connection to the database, and the use of sessions, to one single module, at the very bottom. Ideally (although not completely refactor in this instance) this module should return dictionaries/objects with the information for the resources layer. This way even if we change the database or the names of the fields (like I had to do when defining the foreign key relation ships) we would only need to change those things at this level.

### Installation
I have chosen to use a postgres database in a docker container for ease of use. To set it up the way I have it:
- docker pull postgres
- mkdir -p $HOME/docker/volumes/postgres
- docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres
- psql -h localhost -U postgres -d postgres (to connect to it. I haven't changed the database to another one nor the permissions/role for lack of timebut I am aware that this is not best practices at all)
Once it is running, we can use the included script create_test_database.py to initialize and populate the db. For that:
- create a config.py file as in family_tree/config.py
- add USER=postgres PASSWORD=docker in it (I am not adding that file if only out of muscle memory of not pushing passwords)
- run the script
At this point you should have a small test family in there
NOTE: all of this happens from inside the pipenv environment to make use of the installed libraries

### Time
The coding time for the operations has been around 5 hours. However, the coding time of fighting the creation of the models has been a few hours more, especially when fighting the following:
- Double foreign key from the same table (parent-child edge table)
- Finding a way in python 3 to pass the session from the app to the blueprints (in the code base I am used to we use flask_sqlalchemy_scope which seems to have disappeared in version 2.3.2 of flask_sqlalchemy, leaving me quite lost there). I am painfully aware that I should be using a better context for that session, ideally a request one that closes after each request... lack of time and expertise on this area).
- Trying to find a way to set the constraints in sqlalchemy to disallow permutations of the primary key (I haven't been able to resolve this, but if this was a real application, I would enforce that uniqueness on submission).


