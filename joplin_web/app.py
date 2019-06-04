# coding: utf-8
"""
   joplin-web sauce starlette
"""
# starlette
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# uvicorn
import uvicorn

from joplin_api import JoplinApi

templates = Jinja2Templates(directory="templates")
statics = StaticFiles(directory="static")

app = Starlette()
app.debug = True
app.mount('/static', StaticFiles(directory="static"))

# @TODO get the token from a config file or something
joplin = JoplinApi(token="TOBEDEFINED!")


async def paginator(request, res):
    """
    paginator to limit the flow of the data to render
    :param request:
    :param res:
    :return:
    """
    note_per_page = 20
    page = int(request.query_params['page']) if 'page' in request.query_params else 0
    start = 0
    end = note_per_page
    if page > 0:
        start = note_per_page * page
        end = note_per_page * (page + 1)
    if len(res.json()) >= end:
        payload = res.json()[start:end]
    else:
        if page == 0:
            payload = res.json()[0:len(res.json())]
        else:
            payload = res.json()[note_per_page * (page - 1):note_per_page * page]
    return payload


@app.route('/', methods=['GET'])
async def home(request):
    """
        homepage
    """
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)

"""
    get stuff : folders, notes, tags
"""
@app.route('/api/jw/folders/', methods=['GET'])
async def get_folders(request):
    """
    all the folders
    :param request:
    :return:
    """
    res = await joplin.get_folders()
    return JSONResponse(res.json())


@app.route('/api/jw/notes/', methods=['GET'])
async def get_notes(request):
    """
    all the notes
    :param request:
    :return:
    """
    res = await joplin.get_notes()
    payload = await paginator(request, res)
    return JSONResponse(payload)


@app.route('/api/jw/tags/', methods=['GET'])
async def get_tags(request):
    """
    all the tags
    :param request:
    :return:
    """
    res = await joplin.get_tags()
    return JSONResponse(res.json())


@app.route('/api/jw/notes/folder/{folder}', methods=['GET'])
async def get_notesbyfolder(request):
    """
    get the notes of the given folder
    :param request:
    :return:
    """
    folder = request.path_params['folder']
    res = await joplin.get_folders_notes(folder)
    payload = await paginator(request, res)
    return JSONResponse(payload)


@app.route('/api/jw/notes/tag/{tag_id}', methods=['GET'])
async def get_notesbytag(request):
    """
    get the all the notes related to the tag id
    :param request:
    :return:
    """
    tag_id = request.path_params['tag_id']
    res = await joplin.get_tags_notes(tag_id)
    return JSONResponse(res.json())


@app.route('/api/jw/notes/{note_id}', methods=['GET'])
async def get_note(request):
    """
    get one note by its id
    :param request:
    :return:
    """
    note_id = request.path_params['note_id']
    res = await joplin.get_note(note_id)
    return JSONResponse(res.json())


@app.route('/api/jw/notes/{note_id}/tags/', methods=['GET'])
async def get_notes_tags(request):
    """
    get the tags related to the note id
    :param request:
    :return:
    """
    note_id = request.path_params['note_id']
    res = await joplin.get_notes_tags(note_id)
    return JSONResponse(res.json())


"""
    create stuff : note, folder, tag 
"""
@app.route('/api/jw/notes/', methods=['POST'])
async def create_notes(request):
    payload = await request.json()
    title = payload['title']
    body = payload['body']
    parent_id = payload['parent_id']
    res = await joplin.create_note(title=title, body=body, parent_id=parent_id)
    return JSONResponse(res.json())

# Update note
@app.route('/api/jw/notes/{note_id}', methods=['PATCH'])
async def update_note(request):
    payload = await request.json()
    note_id = payload['note_id']
    title = payload['title']
    body = payload['body']
    parent_id = payload['parent_id']
    res = await joplin.update_note(note_id=note_id, title=title, body=body, parent_id=parent_id)
    return JSONResponse(res.json())

# Delete note
@app.route('/api/jw/notes/{id}', methods=['DELETE'])
async def delete_note(request):
    note_id = request.path_params['id']
    res = await joplin.delete_note(note_id)
    return JSONResponse(res.json())

# create folder
@app.route('/api/jw/folders/', methods=['POST'])
async def create_folder(request):
    folder = await request.json()
    res = await joplin.create_folder(folder=folder['title'])
    return JSONResponse(res.json())

# create tag
@app.route('/api/jw/tags/', methods=['POST'])
async def create_tag(request):
    tag = await request.json()
    res = await joplin.create_tag(title=tag['title'])
    return JSONResponse(res.json())


# HTTP Requests
# Error Pages
@app.exception_handler(404)
async def not_found(request, exc):
    """
    Return an HTTP 404 page.
    """
    template = "404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)


@app.exception_handler(500)
async def server_error(request, exc):
    """
    Return an HTTP 500 page.
    """
    template = "500.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=500)

# Bootstrap
if __name__ == '__main__':
    print('Joplin Web - Starlette powered')
    uvicorn.run(app, host='0.0.0.0', port=8001)
