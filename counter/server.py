from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if 'count' in session:
        print('key exists!')
        session['count'] += 1
        if session['count'] == 1:
            count_str = (f"Visited {session['count']} time")
            print(count_str)
        else:
            count_str = (f"Visited {session['count']} times")
            print(count_str)
        return render_template("index.html", count_str=count_str) #add in count_str = count_str if necessary
    else:
        session['count'] = 0
        count_str=(f"Visited {session['count']} tunes")
        print("key 'key_name' does NOT exist")



@app.route("/counter", methods=["POST"])
def index():
    session['count'] += 1
    return redirect("/")

@app.route("/clear_session", methods=['POST']) #clear the session and redirect to root
def clear_session():
    session.clear()
    session['count'] = 0
    return redirect ('/')


if __name__ == "__main__":
    app.run(debug=True)