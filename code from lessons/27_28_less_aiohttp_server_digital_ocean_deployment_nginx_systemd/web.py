import jinja2
import asyncio
from aiohttp_jinja2 import setup, render_template
from aiohttp import web
from model import Page, objects
from crawler import start_crawl


loop = asyncio.get_event_loop()


async def home_handler(request):
    all_objects = await objects.execute(
        Page.select().distinct(Page.domain).limit(100))
    context = {'objects': all_objects}
    response = render_template('index.html', request, context)
    return response


async def domain_handler(request):
    domain = request.match_info.get('dom')
    all_objects = await objects.execute(
        Page.select().where(Page.domain == domain).limit(1000))
    context = {'pages': all_objects}
    response = render_template('website.html', request, context)
    return response


async def page_handler(request):
    pk = request.match_info.get('pk')
    all_objects = await objects.execute(Page.select().where(Page.id == pk))
    context = {'page': [x for x in all_objects][0]}
    response = render_template('page.html', request, context)
    return response


async def start_crawler(request):
    data = await request.post()
    domain = data['new_domain']
    asyncio.run_coroutine_threadsafe(start_crawl(domain), loop)
    return web.HTTPFound('/')


app = web.Application()

setup(app, loader=jinja2.FileSystemLoader('templates'))


app.add_routes([
    web.get('/', home_handler),
    web.get('/dom/{dom}', domain_handler),
    web.get('/page/{pk}', page_handler),

    web.post('/start_scan', start_crawler),

    web.static('/static', 'static')
])


if __name__ == '__main__':
    web.run_app(app)
