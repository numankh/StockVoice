import hashlib

def hashID(awsUserID):
    encodedID = int(hashlib.sha256(awsUserID.encode('utf-8')).hexdigest(), 16) % 10**8
    return encodedID