from urllib.parse import urlparse


def get_domain_nm(url):
    try:
        domain = get_sub_domain(url).split('.')
        return domain[-2] + '.' + domain[-1]
    except:
        return ''


def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
