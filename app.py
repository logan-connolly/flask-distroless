import pandas as pd
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    # Make sure that library that requires underlying C-libs still works
    s = pd.Series([4, 2, 0, 8])
    result = max(s)
    return f"Hello World! The result is {result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
