data = {    
 'key_1':1,
 'key_2':2, 
 'key_3':[
         {
          'key_4': [4,5],
          'key_5': [6,7]
         },
         {
          'key_4': [8,9],
          'key_5': [10,11]
         }
 ],
 'key_6':12
 }
key = input()
def find_key(data,key):
    if key in data:
        print(data[key])
        return
    
    for k, v in data.items():
         if isinstance(v,list):
            for x in v:
                if isinstance(x,dict) and find_key(x,key) is not None:
                    print(find_key(x,key))
                    return
    print("Does not exist")
    import os
    os._exit(1)
find_key(data,key)
