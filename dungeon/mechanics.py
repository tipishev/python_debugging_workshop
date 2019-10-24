def check_password(player, hexdigest):
    password = player.inventory.pop()
    from hashlib import md5
    password = password.encode('utf8')
    return md5(password).hexdigest() == hexdigest
