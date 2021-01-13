import uvicorn as uvicorn

if __name__ == "__main__":
    uvicorn.run("spa_test:app", port=5000, host="0.0.0.0", reload=True)
