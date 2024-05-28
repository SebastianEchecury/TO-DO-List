import hashlib

def hashPassword(password):
  codedPassword = password.encode('utf-8')
  hashP = hashlib.sha256(codedPassword).hexdigest()
  return hashP

def verifyPassword(password, hashP):
  codedPassword = password.encode('utf-8')
  hashPs = hashlib.sha256(codedPassword).hexdigest()
  return hashPs == hashP

