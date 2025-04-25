
<p align="center">
  <img src="Image/Logo.png" alt="HMS GridGen Logo" width="300"/>
</p>

# HMS GridGen

**HMS GridGen** is a lightweight and user-friendly tool for generating precipitation-frequency grid metadata files for use in **HEC-HMS** models. It takes NOAA Atlas 14 raster grids (`.asc` format), filters them by return period (e.g., 10yr, 50yr, 100yr), and creates a formatted `.grid` file compatible with HEC-HMS.

---

## 🚀 Features

- Filters NOAA `.asc` precipitation grids by specified return periods
- Automatically generates `.grid`-formatted metadata
- Simple web-based user interface using FastAPI
- One-click launch with automatic browser open
- Lightweight virtual environment setup

---

## 📁 Project Structure

```
HMS GridGen/
├── HMS_G_generator/        # Virtual environment (excluded in Git)
├── templates/
│   └── form.html           # Frontend HTML template
├── Image/
│   └── Logo.png            # Project logo
├── main.py                 # FastAPI backend app
├── run_server.py           # Launch script with auto-browser
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/HMS-GridGen.git
cd HMS-GridGen
```

### 2. Create a Virtual Environment
```bash
python -m venv HMS_G_generator
```

### 3. Activate the Environment

#### 🪟 Windows
```bash
HMS_G_generator\Scripts\activate
```

#### 🐧 macOS / Linux
```bash
source HMS_G_generator/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python run_server.py
```

After a few seconds, your default browser will open to:
```
http://127.0.0.1:8502
```

You can now:
- Input the path to your NOAA `.asc` files
- Specify the return periods (comma-separated, e.g., `100yr,50yr,10yr`)
- Click **Generate Grid File**

---

## 📤 Output

The application will generate a file named:

```
filtered_grids_info.txt
```

📌 **Copy and paste its content into your `XXX.grid` file within HEC-HMS.**

---

## 🧹 .gitignore Highlights

This repo excludes:
- Your local virtual environment
- OS temp and cache files
- Binary executables
- Local raster data or intermediate outputs

---

## 📬 Contributions

Feel free to fork this project and submit pull requests. For suggestions or bugs, please open an issue.

---

## ✨ Credits

Developed by [Dr. Mohsen Tahmasebi Nasab](https://www.linkedin.com/in/hydromohsen) – Water Resources Engineer and Educator.

---

## 📄 License

Custom Open-Source License

Copyright (c) 2024 Mohsen Tahmasebi Nasab

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to use, copy, and modify the Software for personal, academic, or internal non-commercial purposes, subject to the following conditions:

1. Commercial use, including but not limited to use in paid services, proprietary software, or as part of any commercial product or package, is not permitted without prior written permission from the copyright holder.

2. Redistribution of the Software, in part or in full, whether modified or unmodified, is also not permitted without prior written permission.

3. This copyright notice and license shall be included in all copies or substantial portions of the Software.

## Disclaimer
The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the author or copyright holder be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software, including but not limited to any direct, indirect, incidental, special, exemplary, or consequential damages.