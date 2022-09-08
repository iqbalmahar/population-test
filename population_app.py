from flask import Flask, request
app = Flask(__name__)

# ...
data = {
    "China":"1425887337",
    "India":"1417173173",
    "UnitedStates":"338289857",
    "Indonesia":"275501339",
    "Pakistan":"235824862",
    "Nigeria":"218541212",
    "Brazil":"215313498",
    "Bangladesh":"171186372",
    "Russia":"144713314",
    "Mexico":"127504125",
}


@app.route('/population', methods=['GET'])
def search():
    args = request.args
    country = args.get('country', default='')
    
    if country not in data.keys():
        return  "Country data does nto exists"
    else:
        return data[country]
