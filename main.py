from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()
app.mount("/", StaticFiles(directory="weblog", html=True))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(loop="asyncio", app='__main__:app', host='0.0.0.0', port=80)

