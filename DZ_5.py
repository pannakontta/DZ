def k_isalpha(s: str):
    i = 0
    while i < len(s):
        if not (65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122):
            return False
        i += 1
    return True


def k_islower(s: str):
    i = 0
    count_low = 0
    while i < len(s):
        if not (65 <= ord(s[i]) <= 90):
            if (97 <= ord(s[i]) <= 122):
                count_low += 1
            i += 1
        else:
            return False
    if count_low > 0:
        return True
    else:
        return False


def k_istitle(s: str):
    i = 0
    count_tit = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
        elif 'A' <= s[i] <= 'Z':
            i += 1
            count_tit += 1
        elif 'a' <= s[i] <= 'z':
            i += 1
        else:
            return False
    if count_tit > 1 or count_tit == 0:
        return False
    else:
        return True
            

def k_upper(s: str):
    i = 0
    up = ''
    while i < len(s):
        if 97 <= ord(s[i]) <= 122:
            k = ord(s[i])
            k -= 32
            up += chr(k)
            i += 1
        else:
            up += s[i]
            i += 1
    return up[0:len(s)]



def k_endswith(s: str, substring: str):
    if s[len(s)-len(substring)::] == substring:
        return True
    return False


def k_count(s: str, substring: str):
    num = 0
    i = 0
    while i < len(s):
        if substring == '':
            num = len(s) + 1
            break
        elif s[i] == substring:
            num += 1
        i += 1
    return num


def k_strip(s: str):
    i = 0
    nachalo = 0
    while i < len(s):
        if not (s[i] == ' '):
            nachalo = i
            break
        else:
            nachalo += 1
        i += 1
    k = 0
    konec = len(s)
    while k < len(s):
        if not (s[len(s) - 1] == ' '):
            break
        if not (s[len(s) - k - 1] == ' '):
            konec -= 1
            break
        else:
            konec = len(s) - k
        k += 1
    return s[nachalo:konec:]


def k_replace(s: str, oldvalue: str, newvalue: str, count: int):
    i = 0
    news = ''
    oldv = 0
    if s == '':
        news = newvalue
    while i < len(s):
        if not s[i:i + len(oldvalue)] == oldvalue:
            news += s[i]
            i += 1
        elif oldv < count:
            news += newvalue
            oldv += 1
            i += len(oldvalue)
        else:
            news += s[i::]
            break
    return news


