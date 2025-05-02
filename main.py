from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Criação da instância do FastAPI
app = FastAPI()

# Configuração do diretório de templates Jinja2
templates = Jinja2Templates(directory="templates")

# Serve arquivos estáticos (como CSS do Bulma)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Lista em memória para armazenar tarefas (simulando um "banco de dados")
todo_items = []

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    # Rota principal: renderiza a página inicial com a lista de tarefas
    return templates.TemplateResponse("index.html", {
        "request": request,
        "todo_items": todo_items
    })

@app.post("/add", response_class=HTMLResponse)
async def add_item(request: Request, item: str = Form(...)):
    todo_items.append({"text": item, "done": False})
    return templates.TemplateResponse("partials/list.html", {
        "request": request,
        "todo_items": todo_items
    })


@app.delete("/delete/{index}", response_class=HTMLResponse)
async def delete_item(request: Request, index: int):
    # Rota para excluir tarefa — também chamada via HTMX
    if 0 <= index < len(todo_items):
        del todo_items[index]
    return templates.TemplateResponse("partials/list.html", {
        "request": request,
        "todo_items": todo_items
    })


@app.patch("/done/{index}", response_class=HTMLResponse)
async def mark_done(request: Request, index: int):
    if 0 <= index < len(todo_items):
        todo_items[index]["done"] = not todo_items[index]["done"]
    return templates.TemplateResponse("partials/list.html", {
        "request": request,
        "todo_items": todo_items
    })
