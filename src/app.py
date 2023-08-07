from aiohttp import web 
from routes.api_routes import api_routes

app = web.Application()
app.router.add_post("/create", api_routes.create_file_pdf)
app.router.add_get("/document/{code}", api_routes.get_file_pdf)

web.run_app(app)