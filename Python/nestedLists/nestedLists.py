if __name__ == '__main__':
    res = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        res.append([name, score])
        
    scores = {score for name, score in res}
    if len(scores)>1:
        scores = sorted(scores)
        second_lowest = scores[1]
    else:
        second_lowest = None
        
    second_lowest_names = [name for name, score in res if score == second_lowest]
    
    second_lowest_names.sort()
    
    for name in second_lowest_names:
        print(name)