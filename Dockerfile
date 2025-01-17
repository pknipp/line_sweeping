FROM nikolaik/python-nodejs:python3.8-nodejs14 as base

WORKDIR /var/www
COPY . .

# Install Python Dependencies
RUN ["pip", "install", "-r", "requirements.txt"]
# RUN ["pip", "install", "psycopg2"]

# Setup Flask environment
ENV FLASK_APP=line_sweeping
ENV FLASK_ENV=production

EXPOSE 8000

# Run flask environment
CMD gunicorn line_sweeping:app
