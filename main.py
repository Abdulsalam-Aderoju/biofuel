from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI() 

app.add_middleware(
   CORSMiddleware,
   allow_origins=['*'],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)




# Allow requests from your frontend's origin
origins = ["https://abdulsalam-aderoju.github.io/Biofuel-Frontend/"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




parameters = ["Density", "Viscosity", "Flash Point", "Heating Value"]

@app.get("/blend-dashboard")
async def blend_info(Density: float,
                     Viscosity: float,
                     Flash_Point: float,
                     Heating_Value: float):

    # Reset validity list and invalid parameters list for each request
    validity = []
    invalid_parameters = []

    if not (775 <= Density <= 840):
        validity.append("Invalid")
        invalid_parameters.append("Density")

    if not (0 <= Viscosity <= 8):
        validity.append("Invalid")
        invalid_parameters.append("Viscosity")

    if not (Flash_Point >= 38):
        validity.append("Invalid")
        invalid_parameters.append("Flash Point")

    if not (42 <= Heating_Value <= 43):
        validity.append("Invalid")
        invalid_parameters.append("Heating Value")

    # Making judgments based on validity list
    if "Invalid" not in validity:
        return "Biofuel meets the requirements in Aviation Industry"
    else:
        invalid_parameters_str = ", ".join(invalid_parameters)
        return f"The following parameters require adjustment: {invalid_parameters_str}"
