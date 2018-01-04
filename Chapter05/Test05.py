mins=[1,2,3]
secs=[min*60 for min in mins]
print(secs)

meters = [1,10,3]
feet = [m * 3.281 for m in meters]
print(feet)

lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

# 定义函数
def sanitize(time_string):
        if '-' in time_string:
                splitter= '-'
        elif ':' in time_string:
                splitter= ':'
        else:
                return(time_string)
        (mins, secs) = time_string.split(splitter, maxsplit = 1)
        return(mins+'.'+secs)
dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)

clean = [float(s) for s in clean]
print(clean)

clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print(clean)
