def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    
    max_str = ""
    max_len = 0
    
    for i in range(len(strarr) - k + 1):
        combined = ''.join(strarr[i:i+k])
        if len(combined) > max_len:
            max_len = len(combined)
            max_str = combined
            
    return max_str

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"],1))