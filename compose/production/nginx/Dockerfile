FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
COPY ./compose/production/nginx/sites-enabled/pulsemanager.conf /etc/nginx/sites-enabled/default
