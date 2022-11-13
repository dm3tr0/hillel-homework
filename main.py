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
        return string.strip('?#')

class HttpUrl(Url):
    def __init__(self, scheme='http', authority=str(), path=list(), query=dict(), fragment=str()):
        super().__init__(scheme, authority, path, query, fragment)

class HttpsUrl(Url):
    def __init__(self, scheme='https', authority=str(), path=list(), query=dict(), fragment=str()):
        super().__init__(scheme, authority, path, query, fragment)

class GoogleUrl(HttpsUrl):
    def __init__(self, scheme='https', authority='google.com', path=list(), query=dict(), fragment=str()):
        super().__init__(scheme, authority, path, query, fragment)

class WikiUrl(HttpsUrl):
    def __init__(self, scheme='https', authority='wikipedia.org', path=list(), query=dict(), fragment=str()):
        super().__init__(scheme, authority, path, query, fragment)

class UrlCreator:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        if self.kwargs['path'] != [*self.kwargs.get('path', []), *args]:
            self.kwargs['path'].clear()
        self.kwargs['path'] = [*self.kwargs.get('path', []), *args]
        self.kwargs['query'] = {**self.kwargs.get('query', {})}
        self.kwargs['query'].update(kwargs)
        return self

    def __getattr__(self, item):
        self.kwargs['path'] = [*self.kwargs.get('path', []), item]
        return UrlCreator(**self.kwargs)

    def _create(self):
        return UrlCreator(**self.kwargs)

    def __str__(self):
        string = self.kwargs['scheme']+'://'+self.kwargs['authority']+'/'
        for i in self.kwargs['path']:
            string = string+i+'/'
        string = string[:-1]
        string += '?'
        if 'query' in self.kwargs.keys():
            for y in self.kwargs['query']:
                string += y+'='+self.kwargs['query'][y]
                string += '&'
        return string.strip('?&/')

    def __eq__(self, other):
        return True if other == str(self) else False
    
#якщо все працює виведеться "еверісінк іс окей"

#завдання 3
assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert str(GoogleUrl()) == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

#завдання 4
url_creator = UrlCreator(scheme='https', authority='docs.python.org')
assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
assert url_creator('api','v1','list') == 'https://docs.python.org/api/v1/list'
assert url_creator('api','v1','list', q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'
assert url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create(), 'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'

print('everything is ok')

