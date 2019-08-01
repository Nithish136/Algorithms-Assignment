'''
    Implementing stack data structure to convert prefix to postfix Notation (Reverse Polish Notation)
'''
class Stack :
    def __init__(self):
        self.stack = []
    def push (self,a):
        self.stack.append(a)
    def pop (self):
        if len(self.stack )< 1:
            return None
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def elements(self):
        return self.stack
    def delete (self):
        self.stack.remove()
    def top (self):
        if len(self.stack) < 1:
            return none
        return self.stack[len(self.stack)-1]
    def is_empty(self):
        if len(self.stack) < 1:
            return True
        return False
'''    
    The below to_postfix function is used to convert the Infix notation to the Postfix By using stack data structure 
''' 

def to_postfix(string):
    for i in string:
        ans = ''
        pres = i
        temp = Stack()
        for j in range(len(pres)):
            if pres[j] in ['+', '-', '*', '^', '/', '(']:
                temp.push(pres[j])
            elif pres[j] == ')':
                pop_e = temp.pop()
                while pop_e != '(' and pop_e != None :
                    ans = ans + pop_e
                    pop_e = temp.pop()
                    #print(ans)
            else:
                ans = ans + pres[j]
    return ans

                
def to_infix (string):
    #print(1,string)
    ans = ''
    pres = string
    #operator = Stack()
    operand =  Stack()
    for j in range(len(pres)):
        if pres[j] not in ['+', '-', '*', '^', '/']:
            operand.push(pres[j])
            #print(j,pres[j])
        elif pres[j] in ['+', '-', '*', '^', '/'] :
            a = operand.pop()
            b = operand.pop()
            if a != None and b!= None:
                temp = b + pres[j] + a 
                operand.push(temp)
        else:
            None

        if j + 1 < len(pres) and (pres[j+1] in  ['*' , '/']) and operand.size() > 1:
            t = operand.pop()
            t = '(' + t + ')'
            operand.push(t)
    ans = operand.pop()
    print(ans)

    
'''
l = Stack()
l.push(23)
l.push(43)
l.push(25)
print(l.elements())
'''
n = int(input())
string = []
for i in range(n):
    string.append(input())
#print(string)
ans = to_postfix(string)

    #print (ans)
to_infix(ans)
