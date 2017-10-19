# Weather Wrapper

This is a weather API that uses Google Cloud Platform to make a wrapper around [OpenWeatherMap](https://openweathermap.org) 
to increase usability and data availability.

**Tech Stack**
* [Google App Engine](https://cloud.google.com/appengine/)
* [Google Cloud Datastore](https://cloud.google.com/datastore/docs/concepts/overview)
* [OpenWeatherMap](https://openweathermap.org)
* [Python 2.7](https://www.python.org/): [Flask](http://flask.pocoo.org/) 

## Setup and development environment

To run a local version or to contribute in the development,
follow these instructions (UNIX):

1. Install the [google cloud sdk](https://cloud.google.com/sdk/docs/quickstart-linux) for python. 

2. Create configuration files.
    * `cp client_secret.json.example client_secret.json`
    * Change the values according to the project configuration (ask main developer).
      
3. Create a virtual environment.
    * `virtualenv -p /usr/bin/python2.7 venv`
    * `source activate venv`
    
4. Install requirements. 
    * `pip install --upgrade -t lib -r requirements.txt`
    
5. Run the local server:
    * `dev_appserver.py app.yaml`
    
You can now test the app at locahost.

## Deployment

1. Deactivate any virtual environment.
    * `source deactivate`

2. Login to your google account.
    * `gcloud auth login`

3. [Optional] Set the project:
    * `gcloud config set project {your-project}`
    
4. [If needed] Update / upload query index.
    * `gcloud datastore create-indexes index.yaml --project {your-project}`
    
5. Upload changes:
    * `gcloud app deploy --project {your-project}`


The app will be running at your project url.  


## Repo Structure

```
|-/app
|   |-/mod_weather
|       |-/model
|       |-/service
|       |-controller.py
|
|-/settings
|
|
|-/util
|
|-/test
|
|-/lib
|-/venv
```

## Contribute


## Authors

* **Rodrigo Hernández Mota** [rhdzmota](https://github.com/rhdzmota) _initial work and main developer_.


## TODO

[ add content ]