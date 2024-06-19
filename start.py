import subprocess
import webbrowser
from threading import Timer
from loguru import logger

def open_browser():
    """Opens a browser window to the frontend."""
    # Ensure the URL matches the expected output from the HTTP server
    webbrowser.open_new('http://localhost:8000/')

def run():
    logger.info("Launching FastAPI backend on port 8001")
    backend = subprocess.Popen(['uvicorn', 'src.backend.app.main:app', '--port', '8001'])

    # Change directory to src/frontend before serving files
    # This step ensures that the simple HTTP server serves files from the correct directory
    import os
    os.chdir('src/frontend')

    logger.info("Serving frontend on port 8000")
    frontend = subprocess.Popen(['python', '-m', 'http.server', '8000', '--directory', '.'])

    # Open the browser window after a slight delay to ensure servers are running
    Timer(1.5, open_browser).start()

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        # Properly handle KeyboardInterrupt to terminate both processes
        backend.terminate()
        frontend.terminate()
        frontend.communicate()  # Ensure frontend subprocess is properly cleaned up
        backend.communicate()   # Ensure backend subprocess is properly cleaned up

if __name__ == '__main__':
    run()
