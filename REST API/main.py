from flask import Flask
import check
app = Flask(__name__)

@app.route("/convert/<string:text>", methods=['GET'])
def convert(text):
    output = check.convert_sp_to_wr(text)
    print(output)
    if output == " H T M L":
        return "HTML"
    else:
        return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
