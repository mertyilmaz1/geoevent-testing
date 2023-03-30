import time

import pandas as pd
from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

df = pd.DataFrame({"name":["iss"], "id":[25544], "latitude":[-37.154849142298], "longitude":[28.986038357665],"altitude":[433.50271238095],"velocity":[27537.123944258],"visibility":["daylight"],"footprint":[4575.5309717821],"timestamp":[1680003604],"daynum":[2460031.8280093],"solar_lat":[2.9303189144016],"solar_lon":[63.217224261698],"units":["kilometers"]})

df["latitude"] = df["latitude"].astype("float64")
df["longitude"] = df["longitude"].astype("float64")
df["altitude"] = df["altitude"].astype("float64")
df["velocity"] = df["velocity"].astype("float64")
df["footprint"] = df["footprint"].astype("float64")
df["daynum"] = df["daynum"].astype("float64")
df["solar_lat"] = df["solar_lat"].astype("float64")
df["solar_lon"] = df["solar_lon"].astype("float64")

df_p = df.T.to_dict('dict')
def update_dfp():
    current_timestamp = time.time()
    df_p[0].update({'timestamp': int(current_timestamp)})
    return df_p[0]
# A route to return all of the available entries in our catalog.
@app.route('/', methods=['GET','POST'])
def api_all():
    with app.app_context():
        return jsonify(update_dfp())


app.config['JSON_AS_ASCII'] = False
if __name__ == "_main_":
    app.run()