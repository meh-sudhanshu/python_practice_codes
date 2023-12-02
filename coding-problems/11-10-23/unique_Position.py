def main():
    _str = "bfbfbfbbfbbfbfbfb"
    visited = [0 for i in range(1000)]
    cp = 0
    visited[cp]=1
    ans = 1
    for ch in _str:
        if ch == 'b':
            if cp-1>=0:
                cp-=1
        else:
            cp+=2
        if visited[cp]!=1:
            ans+=1
            visited[cp]=1
    return ans

print(main())