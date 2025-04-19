from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/run", response_class=HTMLResponse)
def run_script(
    request: Request,
    target_directory: str = Form(...),
    return_periods: str = Form(...)
):
    output_file = os.path.join(target_directory, "filtered_grids_info.txt")
    valid_return_periods = [rp.strip() for rp in return_periods.split(",")]

    # Generate the text output
    template = """Grid: {grid_name}
     Grid Type: Precipitation-Frequency
     Description: NOAA Atlas 14 se Grid
     Units: in/1000
     Last Modified Date: 2 April 2025
     Last Modified Time: 20:13:02
     Data Source Type: ASCII
     Filename: {full_path}
End:

"""
    try:
        all_files = [f for f in os.listdir(target_directory) if f.endswith(".asc")]
        filtered_files = [f for f in all_files if any(rp in f for rp in valid_return_periods)]

        with open(output_file, "w") as out:
            for file in filtered_files:
                grid_name = os.path.splitext(file)[0]
                full_path = os.path.join(target_directory, file)
                entry = template.format(grid_name=grid_name, full_path=full_path)
                out.write(entry)

        message = f"✅ File created successfully at: {output_file}. Please copy and paste this content into your HEC-HMS 'XXX.grid' file."
    except Exception as e:
        message = f"❌ Error: {str(e)}"

    return templates.TemplateResponse("form.html", {"request": request, "message": message})
