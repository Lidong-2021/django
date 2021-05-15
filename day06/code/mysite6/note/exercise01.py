def verification(fun):
    def wrap(*args, **kwargs):
        print('验证账户')
        return fun(*args, **kwargs)

    return wrap


@verification
def deposit(money):
    print('存钱咯', money)


@verification
def withdraw(login_id, pwd):
    print("取钱咯", login_id, pwd)


deposit(100)
withdraw('lily', '123456')
