import requests

class LinkChecker:

    def check_link(self, url):
        try:
            response = requests.request('GET', url, allow_redirects=True)
            if response.status_code == 200 or response.status_code == 201 or response.status_code == 301:
                return True
            else:
                return False
        except Exception as e:
            print('There was a problem reaching that link')
