# TAITOTALO Python programmer course
# UNDER WORK
# NO WARRANTY OR GUARANTEE OF ANY KIND
# USE WITH OWN RISK
import builtins
def substring(a:int,b:int,str_in:str)->str:
    """Get substring with slice exercise

    Args:
        a (int): start
        b (int): end
        str_in (str): String to manipulate
    """
    str_sliced=str_in[a:b]
    #print(str_in[a:b])
    
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
    #print(tmp_str)
    tmp_str=substring(8,-2,str(tmp_str))
    # Check if manipulated type matches types list 
    if type(tmp_str) in [getattr(builtins, d) for d in dir(builtins) if isinstance(getattr(builtins, d), type)]:
        return tmp_str
# 
def is_levels(obj:object)->bool:
    """ Check if object is iterable with iter function

    Args:
        obj (object): Any object

    Returns:
        bool: Boolean return value True (is iterable) or False (is not iterable)
    """
    b_islevels=False
    try:
        iter(obj)
    except Exception:
        b_islevels=False
    else:
        b_islevels= True
    finally:
        return b_islevels
 
#   
def handleItemsRecursively(inObj:object())->str: # :object() is just a hint what should be given to function
    """ Recursively iterate trough any iterable structure
     like tuple,dict,list,collection etc.

    Args:
        iObj (object): Any iterable object

    Returns:
        str: ...
    """
    
    # String is iterable but not wanted to be under iteration
    excluded_iterable_types=["str"]
    iObj=object()
    iObj=inObj
    i=0
    if (iObj.__sizeof__() > 0):
        #    
        for item in iObj:
            item_type=get_typename(item)
            if is_levels(item) == True and item_type not in excluded_iterable_types:
                    print(item)
                    # Recursion starts here
                    handleItemsRecursively(item)
            else:
                print(item)
                #print("Object is not iterable - one level")
                continue
                # End this recursive thread
        #
    #                    
    else:
        print(type(iObj),"Input object is empty.")
    
#
# Testing    
handleItemsRecursively([1,2,3,[4,5,[6,7,8]],9,10,11])
handleItemsRecursively((1,2,3,(4,5,(6,7,8)),9,10,11))
sset={"Set","is","not","nested","iterable","structure"} # Set does not guarantee order of items
ssetX = sset.union({1,2,3,4,5})
handleItemsRecursively(ssetX)
