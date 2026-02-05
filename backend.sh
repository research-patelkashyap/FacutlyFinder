set -e

echo "Starting FastAPI..."
uvicorn FastAPI:app --host 0.0.0.0 --port $PORT
