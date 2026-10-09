import sys
import requests

print(f"python {sys.version.split()[0]} is working!")
r = requests.get("https://api.github.com")
print("Internet/API check: ", r.status_code)