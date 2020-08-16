def sq(n):
    return n**2
a,b,c,d,e = map(int, input().split())
print((sq(a)+sq(b)+sq(c)+sq(d)+sq(e))%10)
