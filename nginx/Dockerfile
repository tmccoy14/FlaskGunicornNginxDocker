# import nginx1.15.8 image
FROM nginx:1.15.8

# remove existing nginx.conf
RUN rm /etc/nginx/nginx.conf

# copy new nginx.conf
COPY nginx.conf /etc/nginx/

# remove existing default.conf
RUN rm /etc/nginx/conf.d/default.conf

# copy new project.conf
COPY project.conf /etc/nginx/conf.d/
