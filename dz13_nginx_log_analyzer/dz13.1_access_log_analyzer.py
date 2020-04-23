import os
import gzip

from log_filter import access_line_filter

base_dir = 'logs'

all_log_files = os.listdir(base_dir)
all_log_files.sort()

result_file = open('results.csv', 'w', encoding='utf-8')
result_file.write('Date\tURL\tGoogle Bot User Agent\n')

results = []

for filename in all_log_files:

    file_path = f'{base_dir}/{filename}'

    if 'error' in file_path:
        continue

    if file_path.endswith('.gz'):
        log_file = gzip.open(file_path)
    else:
        log_file = open(file_path)

    for line in log_file:

        data = access_line_filter(line)

        if not data:
            continue

        ip, ua, url, date = data

        results.append(
            {
                'ip': ip,
                'user_agent': ua,
                'url': url,
                'date': date
            }
        )

        # if date not in result:
        #     result[date] = 1
        # else:
        #     result[date] += 1

    log_file.close()

for result in results:
    result_file.write(f"{result['date']}\t{result['url']}\t"
                      f"{result['user_agent']}\n")
