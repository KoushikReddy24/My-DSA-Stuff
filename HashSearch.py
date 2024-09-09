#create Hash table
hash_table = [[] for i in range(10)]

#find key value and return key value
def hashing(key_value):
    return key_value%len(hash_table)

#inserting in hash table
def insert(hash_table,key_value,value):
    hash_key = hashing(key_value)
    hash_table[hash_key].append(value)

insert(hash_table, 10, 'Allahabad')
insert(hash_table, 25, 'Mumbai')
insert(hash_table, 20, 'Mathura')
insert(hash_table, 9, 'Delhi')
insert(hash_table, 21, 'Punjab')
insert(hash_table, 21, 'Noida')

print(hash_table)

#print hash table
def print(hash_table):
    for i in range(len(hash_table)):
        print(i,end=" ")
    for j in hash_table[i]:
        print("-->",end=" ")
        print(j,end=" ")
    print()