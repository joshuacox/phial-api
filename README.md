Phial API
==================

Phial API is a project that exposes a consistant way to interact with multiple storage engines.  It leverages [django-rest-framework](https://github.com/tomchristie/django-rest-framework) for file uploading, parsing and all the goodies that DRF offers, as well as django storages to add to django's storage engine's.

**With Fig/Docker**

    git clone git@github.com:derek-adair/phial-api.git

**With Fig/Docker**

    # Grab the code
    git clone git@github.com:derek-adair/flex-api.git && cd flex-api
    # spin up the initial containers (this should throw some db errors, django isn't installed)
    fig up
    # FROM YOUR HOST MACHINE: Grab the bower deps (This will be baked in starting 0.0.2)
    cd web/static/web/js && bower install
    # Create a throw-away container and install django / app tables / super user
    fig run --rm web syncdb
    # re-create containers
    fig up
    #App should be running on localhost:8080 via forwarded docker port.

**Manual setup**

If you insist on building this manually, be my guest, but its by far easier to learn/install/use Docker and fig.  Before you can do this I'd suggest working in [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) with python-2.7.

Install psql/psychopg2 deps on Ubuntu (look [here](https://wiki.postgresql.org/wiki/Detailed_installation_guides) for other instuctions):
```
    DEBIAN_FRONTEND=noninteractive && \
    apt-get update -y && \
    apt-get install -y libpq-dev
```
Install python packages
```
    pip install -r requirements.txt
``` 
Set env variables

```
    export AWS_UPLOAD_CLIENT_SECRET_KEY='keep me secret!'
    export AWS_UPLOAD_CLIENT_KEY='who cares if i am secret'
    #not the entire ARN resource, just the bucket name
    export AWS_EXPECTED_BUCKET='your-bucket'
    export AWS_EXPECTED_SIZE='XXXX'
```
Sync/Run it...
```
    ./manage.py migrate
    ./manage.py collectstatic
    ./manage.py runserver 0.0.0.0:8080
``` 
