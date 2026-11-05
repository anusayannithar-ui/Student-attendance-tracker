from fastapi import FastAPI

from connector import connection_new
app = FastAPI()
@app.get("/q={qr_code}")

def query(qr_code:str):
    connection = connection_new() 
    cursor = connection.cursor() 

    cursor.execute("SELECT * FROM students WHERE student_id_hashed_qr_code = %s",(qr_code,))

    




    

