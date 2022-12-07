import copy
def fitness(ch,bspc_t):
    fitness_c = 0
    bspc = copy.deepcopy(bspc_t)
    for i in ch:
        if(i == 'U'):
            bspc[0] = bspc[0] - 1
            if(bspc[0]<0):
                break
            else:
               fitness_c = fitness_c + 1
        if(i == 'D'):
            bspc[0] = bspc[0] + 1
            if(bspc[0]>2):
                break
            else:
               fitness_c = fitness_c + 1
        if(i == 'L'):
            bspc[1] = bspc[1] - 1
            if(bspc[1]<0):
                break
            else:
               fitness_c = fitness_c + 1
        if(i == 'R'):
            bspc[1] = bspc[1] +1
            if(bspc[1]>2):
                break
            else:
               fitness_c = fitness_c + 1
    return fitness_c
def crossover(ch1,ch2,f):
    return ch1[:f] + ch2[f:]
def mutation(ch,f):
    if(ch[f]=='U'):
        ch[f] = 'D'
    elif (ch[f]=='D'):
        ch[f]='U'
    elif (ch[f]=='L'):
        ch[f]='R'
    elif (ch[f]=='R'):
        ch[f]='L'
def GA():
    ch1 = ['U','R','U','D','D','R','L','D']
    ch2 = ['U','L','D','U','D','U','R','R']
    ch3 = ['U','U','R','U','R','U','R','R']
    ch4 = ['R','U','L','U','L','D','R','D']
    blank = [2,0]
    f1 = fitness(ch1,blank)
    f2 = fitness(ch2,blank)
    f3 = fitness(ch3,blank)
    f4 = fitness(ch4,blank)
    print(f1,f2,f3,f4)
    m_f = max([f1,f2,f3,f4])
    while ((f1<8) and (f2<8) and (f3<8) and (f4<8)):
        
        if(f1!=8):
            c1 = crossover(ch1,ch2,m_f)
        if(f2!=8):
            c2 = crossover(ch2,ch1,m_f)
        if(f3!=8):
            c3 = crossover(ch3,ch4,m_f)
        if(f4!=8):
            c4 = crossover(ch4,ch3,m_f)
        f1 = fitness(ch1,blank)
        f2 = fitness(ch2,blank)
        f3 = fitness(ch3,blank)
        f4 = fitness(ch4,blank)
        l_f = min([f1,f2,f3,f4])
        
        c1 = mutation(c1,l_f)
        f1 = fitness(ch1,blank)
        f2 = fitness(ch2,blank)
        f3 = fitness(ch3,blank)
        f4 = fitness(ch4,blank)
GA()
