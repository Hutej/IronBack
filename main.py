from IronBack import IronBack

app = IronBack()

@app.get("/users/{id}")
def get_user(request, response, id):
    response.send(id, "400")

@app.post("/users")
def post_user(request, response):
    response.send('Hey There', "201")
    