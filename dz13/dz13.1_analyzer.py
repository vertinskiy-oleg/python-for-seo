import os
import gzip

from filter import line_filter

base_dir = 'logs'

all_log_files = os.listdir(base_dir)
all_log_files.sort()
print(all_log_files)

result_file = open('results.csv', 'w', encoding='utf-8')
result_file.write('Date\tIp\tUser Agent\tURL\n')

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

        data = line_filter(line)

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
    result_file.write(f"{result['date']}\t{result['ip']}\t"
                      f"{result['user_agent']}\t{result['url']}\n")
