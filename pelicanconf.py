AUTHOR = 'Chia Yuan'
SITENAME = "Nobody's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/teddywang0824'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/Wenqing'
SITETITLE = '微光手札'
SLOGAN = [
    ['是劇中過客 ','亦是書裡路人 ', '興來提筆意隨心'],
    ['拾靈感  ', '寫天真 ', '縫中拾影'],
    ['只為留痕  ', '非是才人']
]
MOTTO = '在縫隙中撿拾光影'
MAIN_MENU = True
MENUITEMS = (('生活與靈感', 'category/inspiration.html'),
             ('程式與科技', 'category/programming.html'),
             ('關於我', 'pages/about.html'),)

DISPLAY_PAGES_ON_MENU = False

DEFAULT_PAGINATION = 10

# Custom CSS (Removed as it is now built-in to the theme)
STATIC_PATHS = ['images','extra', 'blog-image']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
# EXTRA_PATH_METADATA = {
#     'extra/css/custom.css': {'path': 'static/custom.css'}
# }
# CUSTOM_CSS = 'static/custom.css'




PLUGIN_PATHS = ['plugins']
PLUGINS = ['context_patch']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}
