from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Definimos el modelo de Candidato
class Candidato(BaseModel):
    dni: str
    nombre: str
    apellido: str

app = FastAPI()

@app.post("/candidato")
async def crear_candidato(candidato: Candidato):
    # Nos conectamos a la base de datos
    conn = sqlite3.connect('candidatos.db') #si la base de datos tuviese requiriese credenciales, las cargaríamos desde un archivo .env, y lo agaregariamos al git ignore
    cursor = conn.cursor()
    
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS candidatos
                    (dni TEXT PRIMARY KEY, nombre TEXT, apellido TEXT)
                    ''')
    try:
        cursor.execute("INSERT INTO candidatos (dni, nombre, apellido) VALUES (?, ?, ?)",
                       (candidato.dni, candidato.nombre, candidato.apellido))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()  # Hacemos rollback en caso de que el DNI ya exista
        raise HTTPException(status_code=400, detail="DNI introducido ya existe.")
    finally:
        conn.close() 
    
    return {"mensaje": f"Candidato {candidato.nombre} registrado correctamente"} # Si todo ha ido bien
