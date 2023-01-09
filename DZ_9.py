import json
import csv

#Задача 1

# with open('log_100.json') as f:
#     data = json.load(f)
#     d = {}
#     for user in data:
#         ip = user['ip']
#         if ip not in d:
        #     d[f'{ip}'] = 1
        # else:
        #     d[f'{ip}'] += 1
# res = 0
# for key in d:
#     res += d[key]    
# sorted_ip = dict((sorted(d.items(), key = lambda item: item[1], reverse=True))[0:3])
# top = 0
# for key in sorted_ip:
#     print(f'{key}: {sorted_ip[key]} - {sorted_ip[key] / res * 100} %')
#     top += sorted_ip[key] / res * 100 
# unics = 0
# for key in d:
#     if d[key] == 1:
#         unics += 1
# print(f'вклад топ-3 IP: {top} %')
# print('число уникальных IP:', unics)


#Задача 2

# ip_info_dict = {}
# with open('log_full.csv') as f:
#     reader = csv.reader(f)
#     d = {}
#     total = 0
#     for user in reader:
#         total += 1
#         if user[1] not in d:
#             d[f'{user[1]}'] = 1
#         else:
#             d[f'{user[1]}'] += 1
#         ip_info_dict[f'{user[1]}'] = user[2]
# max_amount = max(d.values())
# max_ip = max(d, key=d.get)
# suspicious_agent = {} 
# suspicious_agent['ip'] = max_ip
# suspicious_agent['count'] = max_amount
# suspicious_agent['fraction'] = max_amount / total * 100
# suspicious_agent['last'] = 0
# print(suspicious_agent)

p = 11
q = 7
print(p & q)