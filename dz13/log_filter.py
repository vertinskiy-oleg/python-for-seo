import re


def access_line_filter(line):
    if type(line) is bytes:
        line = line.decode()

    try:

        ip = line.split()[0]
        user_agent = line.strip().split('"')[-4]
        url = line.strip().split('"')[1].split()[1]
        date = line.split()[3][1:].split(':')[0]

    except Exception:
        print('[Error in line]', line)
        return

    if 'google' not in user_agent.lower():
        return

    return ip, user_agent, url, date


def error_line_filter(line):
    date = re.search(r"(\d{4}/\d{2}/\d{2})", line).group(0)
    url = re.search(r"\"(/.*)\"", line).group(0)
    error = re.search(r"\s\((.*)\)", line).group(0)

    print(date, url, error)

    # if type(line) is bytes:
    #     line = line.decode()
    #
    # try:
    #
    #     date = line.split()[3][1:].split(':')[0]
    #
    # except Exception:
    #     print('[Error in line]', line)
    #     return

    # return ip, user_agent, url, date


log = '2020/02/03 15:54:34 [error] 6#6: *1746 open() ' \
      '"/py4you/static_root/certificates/Python%20for%20SEO%20Basic%20%7C%20Dec%202018/maksim-geraschenko.jpg" failed ' \
      '(2: No such file or directory), client: 172.69.135.88, server: py4you.com, request: "GET ' \
      '/static/certificates/Python%2520for%2520SEO%2520Basic%2520%257C%2520Dec%25202018/maksim-geraschenko.jpg ' \
      'HTTP/1.1", host: "py4you.com" '

error_line_filter(log)
