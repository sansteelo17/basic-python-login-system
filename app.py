helloMsg = print('Welcome! Create your account')

createAccUser = input('Input username:')
createAccPass = input('Input password:')

if(createAccUser and createAccPass):
    successMsg = print('User ' + createAccUser + ' created successfully')
    loginMsg = print('Now, login to your account:')

    loginAccUser = input('Input username:')
    loginAccPass = input('Input password:')

    if(loginAccPass and loginAccUser):
        if(loginAccUser == createAccUser and loginAccPass == createAccPass):
            print('User logged in successfully')
        else: print('Invalid credentials')