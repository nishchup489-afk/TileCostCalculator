from fastapi import FastAPI , Request , Response , Form 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import math


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()





def calculate_cost(tile_price, tile_area, room_width, room_height):

    room_area = room_width * room_height

    tiles_needed = math.ceil(room_area / tile_area)

    total_cost = tiles_needed * tile_price

    return tiles_needed, total_cost





templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))
app.mount("/static" , StaticFiles(directory= str(BASE_DIR/"static")) , name="static")


@app.get("/" , response_class=HTMLResponse)
def Home(request: Request):
    return templates.TemplateResponse(
        "index.html" , 
        {"request" : request}
    )


@app.post("/calc" , response_class=HTMLResponse)
def calculate(request: Request , 
              tiles_price : float = Form() , 
              tile_area : float = Form() , 
              room_width : float = Form() , 
              room_height : float = Form()
              ):
    result = calculate_cost(tiles_price , tile_area , room_width , room_height)
    return templates.TemplateResponse(
        "index.html" , 
        {
            "request" : request , 
            "result" : result
        }
    )
