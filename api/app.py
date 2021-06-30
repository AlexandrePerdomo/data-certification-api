
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()


# define a root `/` endpoint
@app.get("/")
def index():
	return {"ok": True}


# Implement a /predict endpoint
@app.get("/predict")
def index(acousticness,danceability,duration_ms,energy,
		  explicit,id,instrumentalness,key,liveness,loudness,
		  mode,name,release_date,speechiness,tempo,valence,artist):
	data = dict(
        acousticness=float(acousticness),
        danceability=float(danceability),
        duration_ms=int(duration_ms),
        energy=float(energy),
        explicit=int(explicit),
        id=id, 
        instrumentalness=float(instrumentalness), 
        key = int(key), 
        liveness= float(liveness),
        loudness = float(loudness), 
        mode=int(mode), 
        name=name,
        release_date= release_date,
        speechiness=float(speechiness), 
        tempo=float(tempo),
        valence=float(valence),
        artist=artist
	)
	data_df = pd.DataFrame(data, index=[0])
	model = joblib.load('model.joblib')
	popularity = model.predict(data_df)

	return {
		"artist": artist,
		"name": name,
		"popularity": popularity,
	}