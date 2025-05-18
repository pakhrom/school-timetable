try:
    from secretsVariables import *
except ModuleNotFoundError:
    import os
    mongoDBURL = os.environ.get("mongoDBURL")
    JWTSecretKey = os.environ.get("JWTSecretKey")