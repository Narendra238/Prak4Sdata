def addCircularLL(linkedList,newData):#menambah data circular
    newNode = {'Data': newData, 'Next':None}
    
    if not linkedList:    
        newNode['Next'] = newNode
        return newNode
    else :
        tempLL = linkedList
        
        while tempLL['Next'] != linkedList:
            tempLL = tempLL['Next']
        
        tempLL['Next'] = newNode
        newNode['Next'] = linkedList
        
        return linkedList
    
def accessCircularLLBelakang(linkedlist):# Membalik data cirular dari belakang
    if not linkedlist:
        return None
    
    current = linkedlist
    data_list = []
    
    while True:
        data_list.append(current['Data'])
        current = current['Next']
        if current == linkedlist:
            break
        
    return data_list[::-1]

def accessCircularLLDepan(linkedlist):# Membalik data cirular dari depan
        if not linkedlist:
            return None
        
        current = linkedlist
        data_list = []
        
        while True:
            data_list.append(current['Data'])
            current = current['Next']
            if current == linkedlist:
                break
            
        return data_list[::1]

def getCircullarAfter(linkedList,key,newData):#Menambah data diantara
    newNode = {'Data' : newData, 'Next':None}
    if not linkedList:
        newNode['Next'] = newNode
        return newNode
    else :
        tempLL = linkedList
        while tempLL:
            if tempLL['Data'] == key:
                newNode['Next'] = tempLL['Next']
                tempLL['Next'] = newNode
                newNode['Next'] = tempLL['Next']['Next']
                tempLL['Next'] = newNode
                return linkedList
            tempLL = tempLL['Next']
            
def deleteNode(linkedlist, key):#menghapus dengan kata kunci 
    current = linkedlist
    while current['Next']:
        if current['Next']['Data'] == key:
            current['Next'] = current['Next']['Next']
            return linkedlist
    current = current['Next']
def deleteHeadNode(linkedList,key):#menghapus dengan kepala 
    if linkedList is None:
        return None
    if linkedList['Data'] == key:
        if linkedList['Next'] is linkedList:
            return None
        else:
            tempLL = linkedList
            while tempLL['Next'] != linkedList:
                tempLL = tempLL['Next']
            tempLL['Next'] = linkedList['Next']
            return tempLL['Next']
    current = linkedList
    while current['Next'] != linkedList:
        if current['Next']['Data'] == key:
            current['Next'] = current['Next']['Next']
            return linkedList
        current = current['Next']
    return linkedList
        
        

def addCircularLLAtTail(linkedList, newData) :#Menambah data dari ekor
  newNode = {'Data' : newData, 'Next' : None}
  
  if not linkedList:
    newNode['Next'] = newNode
    return newNode
  else:
    tempLL = linkedList
    while tempLL['Next'] != linkedList:
      tempLL = tempLL['Next']

    tempLL['Next'] = newNode
    newNode['Next'] = linkedList
    
    return linkedList 

def deleteAtTail(linkedList):#Hapus Di Ekor
    if linkedList is None:
        return None
    
    if linkedList['Next'] == linkedList:
        return None
    
    current  = linkedList
    previous = None
    
    while current['Next'] != linkedList:
        previous = current
        current = current['Next']
        
    previous['Next'] = linkedList
    return linkedList
      
#main
linkedList = None
linkedList = addCircularLL(linkedList,1)
addCircularLL(linkedList,5)
addCircularLL(linkedList,10)
print("Menambah Data : ",linkedList)

getCircullarAfter(linkedList,5,8)
print("Menambah Data Diantara Node : ",linkedList)

addCircularLLAtTail(linkedList,90)
print("Data Ditambah dari ekor : ",linkedList)

data_circullar_acces =  accessCircularLLDepan(linkedList)
print("Data Depan Ke Belakang : ",data_circullar_acces)

data_circullar_acces =  accessCircularLLBelakang(linkedList)
print("Data Belakang Ke Depan : ",data_circullar_acces)

deleteHead = deleteHeadNode(linkedList,1)
print("Menghapus Head : ",deleteHead)

deleteNode(deleteHead,8)
print("Menghapus data dengan key : ",linkedList)

deleteAtTail(deleteHead)
print("Data Hapus Ekor : ",linkedList)


