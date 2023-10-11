dict = {
    'LOL' : 'Laugh out Loud',
    'IDK' : "I don't know",
    'TBH' : 'to be honest'
}

# In this we can make the program still running eventhough there is an excepton 
try: 
   definition = dict['BTW']
   print('Defintion of' , dict , ' is ' , definition)
except:
   print('The key is not present in the dictionary' , dict)
finally:
    print('The dict we have defined are:')
    for key in dict:
        print(key)
