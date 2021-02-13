from fastapi import FastAPI, BackgroundTasks
from fastapi.staticfiles import StaticFiles
import asyncio, httpx, subprocess

app = FastAPI()
app.mount("/", StaticFiles(directory="weblog", html=True))

async def auto_pull():
    subprocess.Popen(["git", "pull"], cwd="weblog")
    repo_url = 'https://api.github.com/repos/PHIKN1GHT/phikn1ght.github.io'
    async with httpx.AsyncClient() as client:
        last_upd = (await client.get(repo_url)).json()['updated_at']
        print('LAST UPDATE: {}'.format(last_upd))
        while True:
            await asyncio.sleep(60)
            updtime = (await client.get(repo_url)).json()['updated_at']
            if not updtime == last_upd:
                print('NEW UPDATE: {}'.format(updtime))
                subprocess.Popen(["git", "pull"], cwd="weblog")
                last_upd = updtime

@app.on_event("startup")
async def onStartup():
    asyncio.create_task(auto_pull())

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(loop="asyncio", app="__main__:app", host='0.0.0.0', port=8000, log_level='debug')
