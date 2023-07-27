# 1. Install uvicorn and fastapi
# pip install fastapi uvicorn

# 2. Imports Libraries
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

# 3. Create App
app = FastAPI()

# 4. Configure CORS to access API from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 5. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello World'}

# 6. Run App
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

# 7a. Using GET Method
@app.get("/predictDisease")
def getPredictDisease(Age_of_the_patient: float,Gender_of_the_patient: float, 
                      Alkphos_Alkaline_Phosphotase: float,Sgpt_Alamine_Aminotransferase: float,ALB_Albumin: float,
                      A_G_Ratio_Albumin_and_Globulin_Ratio: float):
    rgModel = pickle.load(open("rf.pkl", "rb"))
    
    prediction = rgModel.predict([[Age_of_the_patient,Gender_of_the_patient,Alkphos_Alkaline_Phosphotase,Sgpt_Alamine_Aminotransferase,ALB_Albumin,A_G_Ratio_Albumin_and_Globulin_Ratio]])
    return [{
        'Result': str(prediction[0])
    }]

# 7b. Using POST Method

#-------------
# 8. Run the API with uvicorn with Reload Option - Auto Run after edit source code
# uvicorn app:app --reload

# 9. Test API from Web Browser
# http://127.0.0.1:8000/predictPrice?Area=1400&BedRooms=3&BathRooms=3
