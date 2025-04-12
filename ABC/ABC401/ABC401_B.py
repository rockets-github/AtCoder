N = int(input())
error_cnt = 0
login_status = False

for i in range(N):
    action = input()

    match action:
        case "login":
            login_status = True
        case "logout":
            login_status = False
        case "public":
            pass
        case "private":
            if not login_status:
                error_cnt += 1

print(error_cnt)