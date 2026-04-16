from IronBack import IronBack

app = IronBack()

@app.get("/users")
def get_user(request, response):
    response.send(400, "400")

@app.post("/users")
def post_user(request, response):
    response.send('Hey There', "201")
