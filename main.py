from flask import Flask, request, redirect

app = Flask(__name__)

known_shortcuts = {
    'gh': dict(name="GitHub", default="https://github.com/", search="https://github.com/search?q="),
    'msg': dict(name="Messenger", default="https://www.messenger.com", search="https://www.messenger.com"),
    'bb': dict(name="BitBucket", default="https://bitbucket.org/", search="https://bitbucket.org/dashboard"
                                                                          "/repositories?search="),
    'g': dict(name="Google", default="https://www.google.com", search="https://www.google.com/search?q=")
}


@app.route("/<path:param>")
def find(param=''):
    parameters = param.split(" ")
    cmd = parameters[0]
    parameters = parameters[1:]
    if cmd not in known_shortcuts.keys():
        return redirect(known_shortcuts['g']['search'] + str(parameters)[2:-2].replace(",", " "))
    elif len(parameters) == 0:
        return redirect(known_shortcuts[cmd]['default'])
    else:
        return redirect(known_shortcuts[cmd]['search'] + str(parameters)[2:-2].replace(",", "%20%"))


if __name__ == '__main__':
    app.run(port=8000)
