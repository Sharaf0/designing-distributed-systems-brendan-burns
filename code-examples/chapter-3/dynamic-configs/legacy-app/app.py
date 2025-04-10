# app.py - Legacy application
import time
import os
import signal
import json

CONFIG_FILE = '/shared/config.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def handle_sighup(signum, frame):
    print("Received SIGHUP signal. Reloading configuration...", flush=True)
    config = load_config()
    print("Updated configuration:", config, flush=True)

# Register SIGHUP handler
signal.signal(signal.SIGHUP, handle_sighup)

print("Starting legacy application...", flush=True)
config = load_config()
print("Initial configuration:", config, flush=True)

print("Legacy application is running...", flush=True)
# Simulate application running
while True:
    time.sleep(1)