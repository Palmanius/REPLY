with open("Task1\\Input.txt","r") as Input:
    with open("Task1\\Output.txt","w") as Output:
        T = int(Input.readline().strip())

        for cases in range(1,T+1):
            



            solution = 0
            Output.writelines("Case #"+str(T)+": "+str(solution)+"\n")