from time import sleep, time


keywords = '''
write my essay
essay writing service
essayyoda
buyessayclub
pay for essay
essay help
essay shark
masterpapers
'''.strip().split('\n')


# count = 0
#
# while count < 20:
#     count += 1
#     if count % 2 == 0:
#         continue
#     if count == 15:
#         break
#     print(count, keywords)


# t_start = time()
#
# while True:
#     print('Send request to GOOGLE')
#     sleep(3)
#
#     t_now = time()
#
#     if (t_now - t_start) > 30:
#         break


# while True:
#     url = input('Enter URL: ')
#
#     if ('http' in url) and ('//' in url):
#         print('Good Job!')
#         break
#     else:
#         print('You entered bad data. Please, try again!')


for _ in range(5):
    url = input('Enter URL: ')

    if ('http' in url) and ('//' in url):
        print('Good Job!')
        break
    else:
        print('You entered bad data. Please, try again!')


# i = 0
# max_i = len(keywords)
#
# while i < max_i:
#     print(keywords[i])
#     i += 1
#
#
# for elem in keywords:
#     print(elem)
