from fastapi import FastAPI, UploadFile, File
from sql_app import models
from .database import SessionLocal, engine
from sql_app.services.excel_parser import parse_excel
from fastapi.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/upload_check_and_parse_xlsx/")
async def upload_check_and_parse_xlsx(file: UploadFile = File(...)):
    try:
        # Проверка, что файл имеет расширение .xlsx
        if not file.filename.endswith(".xlsx"):
            return JSONResponse(content={"error": "Неверное расширение файла"}, status_code=400)

        # Парсинг всего файла Excel с использованием pandas
        parsed_data = parse_excel(file.file)

        return JSONResponse(content={"message": "Файл XLSX успешно загружен и распарсен", "data": parsed_data})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
