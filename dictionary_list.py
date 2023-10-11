menu = {
    'breakfast' : [ 'chapathi ' , 'dosa'] ,
    'lunch' : [ 'Pulav ' , 'Rice'],
    'dinner' : ['Roti', 'curry']   
}


for key in menu:
    print( key )
    
for key , value in menu.items() :
    print (key ," : " , value)