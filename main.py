from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

from vehicle import Motorcycle,Car,Truck,Bus
from price import Pricing
from garage import Level,Garage
from exceptions import ParkingException

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="templates")

garage = None

class SetupRequest(BaseModel):
    num_levels:int
    spots_per_level:int

class ParkRequest(BaseModel):
    reg_num:str
    size:str

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(request=request,name="index.html")

@app.post("/api/setup")
async def setup_api(request:SetupRequest):
    global garage
    levels_list=[]
    for i in range(request.num_levels):
        levels_list.append(Level(f"Level {i+1}",request.spots_per_level))

    garage=Garage(levels_list,Pricing())
    return {"success": True, "message": f"Garage created with {request.num_levels} levels"}

@app.post("/api/park")
async def park_api(request:ParkRequest):
    global garage
    Reg_num=request.reg_num
    v_type=request.size
    if v_type=='1':
        vehicle=Motorcycle(Reg_num)
    elif v_type=='2':
        vehicle=Car(Reg_num)
    elif v_type=='3':
        vehicle=Truck(Reg_num)
    elif v_type=='4':
        vehicle=Bus(Reg_num)
    else:
        return {"success": False, "error": "invalid code"}

    try:
        ticket=garage.park(vehicle)
        return {"success": True, "message": f"Parked: {ticket}"}
    except ParkingException as e:
        return {"success": False, "error": f"Parking failed: {e}"}


    if __name__=="__main__":
        uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
