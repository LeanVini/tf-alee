import os

INSTANCE_ID = os.getenv('INSTANCE_ID', 'unknown')
LOAD_FACTOR = float(os.getenv('LOAD_FACTOR', 1.0))

RESPONSE_DELAY = 0.1 * LOAD_FACTOR  # Simula diferentes cargas

