
x = "Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure."

b = x.rfind(' ',0)

print(b)
print(x[:b])
print(x[:b].strip())
print(len(x[:b]))
print(len(x[:b].strip()))
c = x.rfind(' ',100)
print(c)


def clip(text, max_len=80):
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
    if space_before >= 0:
        end = space_before
    else:
        space_after = text.rfind(' ', max_len)
    if space_after >= 0:
        end = space_after
    if end is None: # no spaces were found
        end = len(text)
    return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

from inspect import signature
sig = signature(clip)
print(sig)
