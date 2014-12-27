Flex Gallery
==================

Flex gallery is a very simple API that stores photos in an amazon S3 bucket paired with a JS client that is mobile friendly!

(honestly not that impressive and needs tests, may not be working right now... just wanted to put it somewhere.)

    git clone git@github.com:derek-adair/flexgallery.git
    fig run web migrate
    fig up
    
Set environment variables

    export AWS_CLIENT_SECRET_KEY='keep me secret!'
    export AWS_SERVER_PUBLIC_KEY='who cares if i am secret'
    export AWS_SERVER_PRIVATE_KEY='keep me secret!'
