Flex Gallery
==================

Flex gallery is a mobile ready gallery paired with a [django-rest-framework](https://github.com/tomchristie/django-rest-framework) API for maximum flexibility.  Using a [django upload package](https://github.com/derek-adair/django-fine-uploader) it is capable of storing files in a number of backends (S3, local storage, Azure, Mongo, etc).


**With Fig/Docker**

    git clone git@github.com:derek-adair/flexgallery.git
    fig run web migrate
    fig run web collectstatic
    fig up

**Without Fig/Docker**

If you insist on building this manually, be my guest, but its by far easier to learn/install/use Docker and fig.  Before you can do this I'd suggest working in [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) with python-2.7.

Install psql/psychopg2 deps on Ubuntu (look [here](https://wiki.postgresql.org/wiki/Detailed_installation_guides) for other instuctions):

    DEBIAN_FRONTEND=noninteractive && \
	apt-get update -y && \
	apt-get install -y libpq-dev

Install python packages
    pip install -r requirements.txt
    
Set env variables
    export AWS_UPLOAD_CLIENT_SECRET_KEY='keep me secret!'
    export AWS_UPLOAD_CLIENT_KEY='who cares if i am secret'
    #not the entire ARN resource, just the bucket name
    export AWS_EXPECTED_BUCKET='your-bucket'
    export AWS_EXPECTED_SIZE='XXXX'

Sync/Run it...
    ./manage.py migrate
    ./manage.py collectstatic
    ./manage.py runserver 0.0.0.0:8080
    
