import subprocess
import webbrowser
from threading import Timer

def open_browser():
    """Opens a browser window to the frontend."""
    webbrowser.open_new('http://localhost:8000/frontend/')

def run():
    # Run the FastAPI backend
    backend = subprocess.Popen(['uvicorn', 'backend.main:app', '--port', '8001'])

    # Serve the frontend on port 8000
    frontend = subprocess.Popen(['python', '-m', 'http.server', '8000'])

    # Open the browser window
    Timer(1.5, open_total_coderondaya_image).start()

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        backend.terminate()
        frontend.terminate()

if __name__ == '__main__':
    run()
