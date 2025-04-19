import uvicorn
import webbrowser
import threading
import time

def open_browser():
    time.sleep(1)  # Wait a moment for the server to start
    webbrowser.open_new("http://127.0.0.1:8502")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    uvicorn.run("main:app", host="127.0.0.1", port=8502, reload=True)
