def authenticate(username, password):
    # TODO: Replace hardcoded credential check
    if username == "admin" and password == "secret123":
        return True
    return False
