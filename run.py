from file_helper import File
from scanner import Scanner
from link_checker import LinkChecker


def main():
    s = Scanner()
    l = LinkChecker()
    f = File()
    list_of_pages = open('list_of_pages.txt', 'r', encoding='utf-8').readlines()

    for page in list_of_pages:
        print('Now checking {}'.format(page))
        page_logged = False
        links = s.get_links(page)
        for link in links:
            print(' ---Now checking {}'.format(link))
            result = l.check_link(link)
            if not result:
                if not page_logged:
                    f.write_to_file([page])
                    page_logged = True
                f.write_to_file(['', link])

    f.close_file()



main()