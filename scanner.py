from requests_html import HTMLSession

class Scanner:

    def __init__(self):
        self.session = HTMLSession()

    def get_raw_html(self, url):
        result = self.session.get(url)
        return result.html
        
    def get_rendered_html(self, url):
        result = self.session.get(url)
        result.html.render()
        return result

    def get_links(self, url):
        result = self.get_rendered_html(url)
        a_s = result.html.find('a')
        links = []
        try:
            for a in a_s:
                if 'href' in a.attrs and 'http' in a.attrs['href']:
                    links.append(a.attrs['href'])
                elif 'href' in a.attrs and not list(a.absolute_links):
                    a.url + a.attrs['href']
                elif hasattr(a, 'absolute_link'):
                    list(a.absolute_links)[0]
        except Exception as e:
            print(e)
        return links

    


