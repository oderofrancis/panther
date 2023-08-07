from app.apis import hello_world_api, info_api

urls = {
    '/': hello_world_api,
    'info/': info_api,
}
