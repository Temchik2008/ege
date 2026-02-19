def f(start, end, cnt):
    if start == end and cnt <= 15: return 1
    if start > end or cnt > 15: return 0
    return f(start +2, end, cnt + (start +3 )%2) + f(start +3, end, cnt + (start + 2 )%2) + f(start * 2 + 1, end, cnt + (start +3 )%2)

print(f(1, 55, 00))