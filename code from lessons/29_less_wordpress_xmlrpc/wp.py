from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, EditPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media


XML_RPC_API = 'http://wp.py4seo.com/xmlrpc.php'
USER = 'admin'
PASS = 'Admin123456'


wp_client = Client(XML_RPC_API, USER, PASS)

all_posts = wp_client.call(GetPosts())


file = 'Neil-Armstrong.jpg'

data = {
    'name': file,
    'type': 'image/jpeg',
}

# read the binary file and let the XMLRPC library encode it into base64
with open(file, 'rb') as img:
    data['bits'] = xmlrpc_client.Binary(img.read())


response = wp_client.call(media.UploadFile(data))

print(response)

my_post = all_posts[0]
my_post.thumbnail = response['id']

result = wp_client.call(EditPost(my_post.id, my_post))


print(result)

# breakpoint()


# post = WordPressPost()
# post.title = 'Neil Armstrong'
# post.content = '''
# <p>Neil Alden Armstrong (August 5, 1930 – August 25, 2012) was an American astronaut
# and aeronautical engineer and the first person to walk on the Moon. He was also a
# naval aviator, test pilot, and university professor.</p>
#
# <p>A graduate of Purdue University, Armstrong studied aeronautical
# engineering; his college tuition was paid for by the U.S. Navy under
# the Holloway Plan. He became a midshipman in 1949 and a naval aviator
# the following year. He saw action in the Korean War, flying the Grumman
# F9F Panther from the aircraft carrier USS Essex. In September 1951, while
# making a low bombing run, Armstrong's aircraft was damaged when it collided
# with an anti-aircraft cable which cut off a large portion of one wing.
# Armstrong was forced to bail out. After the war, he completed his bachelor's
# degree at Purdue and became a test pilot at the National Advisory Committee
# for Aeronautics (NACA) High-Speed Flight Station at Edwards Air Force Base in
# California. He was the project pilot on Century Series fighters and flew the
# North American X-15 seven times. He was also a participant in the U.S. Air
# Force's Man in Space Soonest and X-20 Dyna-Soar human spaceflight programs.</p>
#
# <p>Armstrong joined the NASA Astronaut Corps in the second group,
# which was selected in 1962. He made his first spaceflight as command
# pilot of Gemini 8 in March 1966, becoming NASA's first civilian
# astronaut to fly in space. During this mission with pilot David Scott,
# he performed the first docking of two spacecraft; the mission was
# aborted after Armstrong used some of his re-entry control fuel to
# stabilize a dangerous roll caused by a stuck thruster. During training
# for Armstrong's second and last spaceflight as commander of Apollo 11,
# he had to eject from the Lunar Landing Research Vehicle moments
# before a crash.</p>
# '''
#
# post.terms_names = {
#     'post_tag': ['test', 'firstpost'],
#     'category': ['Introductions', 'Tests']
# }
#
# new_post = wp_client.call(NewPost(post))
#
# print(new_post)
