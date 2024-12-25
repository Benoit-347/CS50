#advanced return for conditonals
def is_odd(a):
    #syn: return <value> if <conditon> else <value>
    return True if a % 2 == 1 else False

if is_odd(4):
    print("odd")
    
#making it shorter as comparison only gives true or false
def is_odd(a):
    return a % 2 ==1