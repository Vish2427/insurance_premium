from flask import Flask
from premium.logger import logging
from premium.exception import PremiumException

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def test():
    try:
        return'Working fine'
    except Exception as e:
        raise PremiumException(e, sys) from e

if __name__=="__main__":
    app.run()