import os
import sys

HOST = "45.9.43.16"
# HOST = "localhost"
PORT = '8090'
API_URL = f'{HOST}:{PORT}'
USERNAME: str = sys.argv[1] if len(sys.argv) == 2 else "чучело"