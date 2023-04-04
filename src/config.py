import os
import sys

# HOST = os.getenv("SERVER_HOST")
HOST = "localhost"
PORT = '8080'
API_URL = f'{HOST}:{PORT}'
USERNAME: str = sys.argv[1] if len(sys.argv) == 2 else "чучело"