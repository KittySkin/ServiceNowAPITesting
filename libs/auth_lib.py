import auth_data.auth_data as auth

# These functions are generics and return the value for the caller, the way to handle getting the data and returning it
# is 100% up to the user. These exist to provide a standard generic API for the caller code.
# Do not hardcode the values to be used. Retrieve them using secrets, decrypting an encrypted file or using a secure
# way to retrieve and set them. Security is a top priority. Never ever commit to a repo or any source control them.

def get_oauth2():
    try:
        return auth.oauth2
    except AttributeError:
        return 'Please ensure the oauth2 variable is set'

def get_instance_url():
    try:
        return auth.instance_url
    except AttributeError:
        return 'Please ensure the instance_url variable is set'

def get_username():
    try:
        return auth.username
    except AttributeError:
        return 'Please ensure the username variable is set'

def get_password():
    try:
        return auth.password
    except AttributeError:
        return 'Please ensure the password variable is set'