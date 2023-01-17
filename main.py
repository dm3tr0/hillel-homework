class HashTable:
    def __init__(self):
        self.MAX_LEIGHT = 100
        self.array = [None for i in range(self.MAX_LEIGHT)]
    
    def get_hash(self, key: str) -> int:
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX_LEIGHT
    
    def add(self, key: str, value):
        hash = self.get_hash(key)
        self.array[hash] = value

    def print(self, key: str):
        print(key, '=', self.array[self.get_hash(key)])

    def delete(self, key:str):
        self.array[self.get_hash(key)] = None

hash_table = HashTable()

hash_table.add('key 1', 'value 1')
hash_table.add('key 2', 'value 2')
hash_table.add('key 3', 'value 3')
hash_table.add('errorkey', 'wrongvalue')

hash_table.print('key 1')
hash_table.print('errorkey')

hash_table.delete('errorkey')
hash_table.print('errorkey')