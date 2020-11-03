#
#
import pickle as pckl
import pandas as pda
import time as tme
import os
import threading
import time
from K9 import __Dog # Dog class from K9.py
## 
class serialize_to_pickle:
    """[serialize_to_pickle class serializes and deserializes serializable object]
    """
    #
    print('Text Object serialization and backwards creation')        
    #print("Text Object serialization and backwards creation")
    is_err=False
    def obj_to_pickle_file(self,obj:object,xstr:str):
        """[serialize_to_pickle serializes object to pickle file]

        Args:
            obj (object): [serializable object]
            xstr (str): [path and name to finished serialized object]

        Raises:
            ex: [Exception]

        Returns:
            [object]: [serialized object as it was]
        """
        #
        try:
            pda.to_pickle(obj,xstr)
            return obj
        #
        except Exception as ex:
            is_err=True
            raise ex
        #
                
    # 
    print('Wait for 5 sec to read pickled file.')    
    #print("Wait for 5 sec to read pickled file.")
    tme.sleep(5)
    #
    is_err=False
    # This block is not tested because of pickle error
    def obj_from_pickle(self,obj:object,xstr:str):
        """[obj_from_pickle deserializes pickle file to object]

        Args:
            obj (object): [deserializable object]
            xstr (str): [path and name to deserializable object]

        Raises:
            ex: [Exception]

        Returns:
            [object]: [deserialized object as it was originally]
        """
        #
        try:
            del obj # delete object - send to garabage collector
            objx=object() # create new object with new name to avoid mixing
            print(xstr) # print path and name
            pda.to_pickle(objx,"./dummy.pkl")
            objx = pda.read_pickle(xstr,None)
            print('Size of opened object is: ',str(objx.__sizeof__()))
            print('IN CLASS: Dog number is: ',objx.number,' Dog name is : ',objx.name,' Dog age is: ',objx.age)
            print('sleep for 5 sec again' )
            tme.sleep(5)
            print('Delete file serialized_obj')
            os.remove(xstr)
            return objx
                
        except Exception as ex:
            is_err=True
            raise ex
        
        else:
            is_err=False
            
                
if __name__ == "__main__":
    stp=serialize_to_pickle()
    obj=object()
    xobj = object()
    obj = __Dog(1,"Rex",1) 
    stp.obj_to_pickle_file(obj,'serialized_obj')
    xobj = stp.obj_from_pickle(obj,'serialized_obj')
    print('Dog number is: ',xobj.number,' Dog name is : ',xobj.name,' Dog age is: ',xobj.age)
                