def main():
    N = int(input())
    
    results = []
    
    case_counter = 0
    
    while case_counter < N:
        X = int(input())
        
        nums = list(map(int, input().split()))
        
        sum_squares = 0
        
        num_counter = 0
        
        while num_counter < X:
            num = nums[num_counter]
            
            if num >= 0:
                sum_squares += num ** 2
            
            num_counter += 1
        
        results.append(str(sum_squares))
        
        case_counter += 1
    
    print("\n".join(results))

if __name__ == "__main__":
    main()