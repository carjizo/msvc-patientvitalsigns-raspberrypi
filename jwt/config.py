#config urls auth

#auth read
AUTH_READ = 'https://msvc-users-production.up.railway.app/oauth2/authorization/msvc-users-client'

#auth read-write
AUTH_READ_WRITE = 'https://msvc-auth-production.up.railway.app/oauth2/authorize?response_type=code&client_id=users-client&scope=read%20write&redirect_uri=https://msvc-users-production.up.railway.app/users/authorized'

#login
AUTH_LOGIN = 'https://msvc-auth-production.up.railway.app/login'
DATA_LOGIN = {
        'username': 'admin',
        'password': '123456'
}
HEADERS_LOGIN = {
        'Content-Type': 'application/x-www-form-urlencoded'
}

#AUHT_JWT
AUTH_JWT = 'https://msvc-auth-production.up.railway.app/oauth2/token'
HEADERS_JWT = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic dXNlcnMtY2xpZW50OjEyMzQ1'
}
REDIRECT_URI = 'https://msvc-users-production.up.railway.app/users/authorized'