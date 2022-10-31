class Url:
    def __init__(self, scheme, authority, path=list(), query=dict(), fragment=str()):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        return True if other == str(self) else False
    
    def __str__(self):
        string = self.scheme+'://'+self.authority
        for i in self.path:
            string += '/'
            string += i
        string += '?'
        for i in self.query:
            string += i+'='+self.query[i]
            string += '&'
        string = string.strip('&')
        string += '#'+self.fragment
        return string

bruh = Url('https', 'google.com', path=['bruh', 'man'], query={'q': 'python', 'result': 'json'}, fragment='que')

print(bruh)
print(bruh == 'https://google.com/bruh/man?q=python&result=json#que')
