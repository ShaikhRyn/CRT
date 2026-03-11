def reverse_number(n: int) -> int:
    p = str(n)      
    q = p[::-1]  
    r = int(q)   
    return r

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))