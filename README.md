# SkySwallower

## Steps to start local development
1) Clone this repository
2) Copy login.txt into the folder
3) Download [GoogleCloud Sql Proxy](https://dl.google.com/cloudsql/cloud_sql_proxy_x64.exe) and run
    'cloud_sql_proxy.exe -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:3306'
4) Run python manage.py runserver 
5) Open localhost:8000/webscraper

## Steps to deploy to google cloud
Follow instructions at [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs/)