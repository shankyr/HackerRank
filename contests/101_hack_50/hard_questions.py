
n = int(raw_input().strip())

vincent = raw_input().strip()
catherine = raw_input().strip()

answer = 0
for i in xrange(n):
    if vincent[i] != catherine[i] and vincent[i] != '.':
        answer += 1

print answer