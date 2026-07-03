def biggest(a,b):
    return a if a>b else b

def pl(cp,sp):
    msg=""
    if sp>cp:
        msg=f"Profit is {sp-cp}"
    else:
        msg=f"Loss is {cp-sp}"
    return msg    