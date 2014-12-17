FROM derekadair/python-2.7

WORKDIR /app
RUN virtualenv /env

# Build Node.js
RUN \
  cd /tmp && \
  wget http://nodejs.org/dist/node-latest.tar.gz && \
  tar xvzf node-latest.tar.gz && \
  rm -f node-latest.tar.gz && \
  cd node-v* && \
  ./configure && \
  CXX="g++ -Wno-unused-local-typedefs" make && \
  CXX="g++ -Wno-unused-local-typedefs" make install && \
  cd /tmp && \
  rm -rf /tmp/node-v* && \
  npm install -g npm && \
  echo -e '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc

# Required for pscopg2
RUN DEBIAN_FRONTEND=noninteractive && \
	apt-get update -y && \
	apt-get install -y libpq-dev

# Install app requirements
ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install -r requirements.txt

ADD . /app
RUN npm install -g bower nvm
RUN cd /app/portfolio/static/js && bower --allow-root install

ENTRYPOINT ["/env/bin/python", "manage.py"]
CMD ["runserver", "0.0.0.0:8080"]

