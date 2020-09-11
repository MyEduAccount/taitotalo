# TAITOTALO Python programmer course
#
def substring(a:int,b:int,str_in:str)->str:
    """Get substring with slice exercise

    Args:
        a (int): start
        b (int): end
        str_in (str): String to manipulate
    """
    str_sliced=str_in[a:b]
    print(str_in[a:b])
    
    return str(str_sliced)
#
#str_1="Testing slice"    
#substring(0,14,str_1)
#
def get_typename(typein:object())->str:
    """Take in any object like int,floatlist etc and hanle type string 

    Args:
        typein (object): Any object type

    Returns:
        str: object type as shorten string
    """
    tmp_str=type(typein)
    tmp_str=substring(8,-2,str(tmp_str))
    
    return tmp_str


# Testing 
ddict={}
print(get_typename(ddict))
nbr_1=9    
print(get_typename(nbr_1))