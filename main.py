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
    print(dates)
    print(ips)
    print(users)
