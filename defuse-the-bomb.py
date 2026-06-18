def decrypt(code, k):
    n = len(code)
    if k == 0:
        return [0] * n
    
    result = []
    if k > 0:
        for i in range(n):
            total = 0
            for j in range(1, k + 1):
                if i + j < n:
                    total += code[i + j]
                else:
                    total += code[(i + j) % n]
            result.append(total)
    else:
        k = abs(k)
        for i in range(n):
            total = 0
            for j in range(1, k + 1):
                if i - j >= 0:
                    total += code[i - j]
                else:
                    total += code[n + i - j]
            result.append(total)
    return result

def decrypt_v2(code, k):
    n = len(code)
    if k == 0:
        return [0] * n
    
    result = [0] * n
    if k > 0:
        total = sum(code[:k])
        result[0] = total
        for i in range(1, n):
            total = total - code[i] + code[(i + k - 1) % n]
            result[i] = total
    else:
        k = abs(k)
        total = sum(code[-k:])
        result[-1] = total
        for i in range(n - 2, -1, -1):
            total = total - code[i + 1] + code[(i - k + 1) % n]
            result[i] = total
    return result