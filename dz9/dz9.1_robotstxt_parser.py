from reppy.robots import Robots

urls = [
    "https://habr.com/ru/search/?q=python",
    "https://habr.com/ru/company/southbridge/blog/489628/",
    "https://habr.com/ru/company/skyeng/blog/487764/",
    "https://habr.com/register/",
    "https://habr.com/ru/users/gbougakov/",
    "https://habr.com/ru/search/?q=django",
    "https://habr.com/ru/post/486998/"
]

robots = Robots.fetch('https://habr.com/robots.txt')

for url in urls:
    print(f"URL {url} is allowed: \
  {robots.allowed(url, 'Googlebot')}")
