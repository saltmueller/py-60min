from bottle import route, run
import time 

@route("/time")
def get_time():
    return { 
        "ms" : time.time(), 
    }

run(host="localhost", port=8080, debug=True)

