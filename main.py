import matplotlib.pyplot as plt

dates  = {}
ips = {}
users = {}
with open('access.log', 'r') as file:
    for line in file:
        args = line.split()
        dates[args[0]] = dates.get(args[0], 0) + 1
        ip = args[3].split(':')[0]
        ips[ip] = ips.get(ip, 0) + 1
        username = args[-1].split('.')[-1]
        users[username] = users.get(username, 0) + 1

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

axes[0].bar(dates.keys(), dates.values(), color='steelblue')
axes[0].set_title('Подключения по датам')
axes[0].set_xlabel('Дата')
axes[0].set_ylabel('Количество')
axes[0].tick_params(axis='x', rotation=45)

axes[1].bar(ips.keys(), ips.values(), color='coral')
axes[1].set_title('Подключения по IP')
axes[1].set_xlabel('IP-адрес')
axes[1].set_ylabel('Количество')
axes[1].tick_params(axis='x', rotation=45)

axes[2].bar(users.keys(), users.values(), color='mediumseagreen')
axes[2].set_title('Подключения по пользователям')
axes[2].set_xlabel('Пользователь')
axes[2].set_ylabel('Количество')
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('diagram.jpg', format='jpg', dpi=150)
print('Диаграмма сохранена: diagram.jpg')
