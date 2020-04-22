from parse_google import parse_google
from image_parser import parse_image
from os import listdir
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPost, NewPost, EditPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media

XML_RPC_API = 'http://wp.py4seo.com/xmlrpc.php'
USER = 'admin'
PASS = 'Admin123456'

wp_client = Client(XML_RPC_API, USER, PASS)

key = input("Enter key: ")

text = ' '.join(parse_google(key))
parse_image(key)
image_path = f"images\\{listdir('images')[0]}"

post = WordPressPost()
post.title = f'Dz29 Vertinskyi Post For Key: {key}'
post.content = text

post.terms_names = {
    'post_tag': ['dz29', key],
    'category': ['vertinskyi', key]
}

new_post = wp_client.call(NewPost(post))

post.post_status = 'publish'
wp_client.call(EditPost(new_post, post))

data = {
    'name': image_path,
    'type': 'image/jpeg',
}

with open(image_path, 'rb') as img:
    data['bits'] = xmlrpc_client.Binary(img.read())

response = wp_client.call(media.UploadFile(data))

my_post = wp_client.call(GetPost(new_post))

my_post.thumbnail = response['id']

result = wp_client.call(EditPost(my_post.id, my_post))