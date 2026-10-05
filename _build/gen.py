"""Gera as páginas do site em pt (raiz), en (en/) e es (es/).

Uso: python3 _build/gen.py
Textos: _build/i18n.py  ·  Ícones SVG: _build/sprite.html
"""
import os
from i18n import LANGS, DIR, HTML_LANG, LOCALE, LANG_NAME, T, PROJ, POST_TX, DATES, QUOTES, ROLES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)  # raiz do repositório
SPRITE = open(os.path.join(HERE, 'sprite.html')).read()
SITE = 'https://natanaellima.blog/'

EXT = 'target="_blank" rel="noopener noreferrer"'
CV = 'https://drive.google.com/file/d/1lg2fYg4_A2yYg5QsX-86DCXbS38xX-Ok/view'
GH = 'https://github.com/ademakin3051'
LI = 'https://www.linkedin.com/in/natanaellima10'
WA = 'https://wa.me/351910617161'
MAIL = 'mailto:natanaellima65@gmail.com'


def i(name):
    return f'<svg class="i" aria-hidden="true"><use href="#i-{name}"></use></svg>'


class Page:
    def __init__(self, lang, page):
        self.lang, self.page = lang, page
        self.up = '../' if DIR[lang] else ''          # caminho até a raiz (assets)

    def t(self, key):
        return T[key][self.lang]

    def asset(self, path):
        return self.up + path

    def url(self, lang=None, page=None):
        """URL absoluta de uma página (para canonical/hreflang)."""
        lang = lang or self.lang
        page = page or self.page
        name = '' if page == 'index' else f'{page}.html'
        return SITE + DIR[lang] + name

    def link_to_lang(self, lang):
        """Link relativo para a mesma página em outro idioma."""
        name = 'index.html' if self.page == 'index' else f'{self.page}.html'
        return self.up + DIR[lang] + name


PROJECTS = [
    dict(id='chatbot-glpi', n='001', name='Chatbot GLPI', img='projeto1',
         tags=['N8N', 'GLPI', 'OpenAI', 'WhatsApp', 'Webhooks'], gh='https://github.com/ademakin3051/botglpi', demo='https://youtu.be/EqQT7VZ-78E'),
    dict(id='digitador-automatico', n='002', name='Digitador Automático', img='projeto2',
         tags=['Python', 'Tkinter', 'Pynput', 'GUI'], gh='https://github.com/ademakin3051/digitador-automatico', demo='https://youtu.be/trLHH-mYcH4'),
    dict(id='script-googledorks', n='003', name='Script GoogleDorks', img='projeto3',
         tags=['Google Dorks', 'API', 'Recon'], gh='https://github.com/ademakin3051/ferramentagoogledorks', demo='https://youtu.be/EfaL-Qc4lK4'),
]


def pname(p, lang):
    return PROJ[p['id']].get('name', {}).get(lang, p['name'])


POSTS = [
    dict(key='japan', cat='Cyber News', date='2025-01-11', min=5, img='blogdestaque', alt='Japan Uncovers Chinese Hacker', lang='en',
         title='Japan Uncovers Chinese Hacker Behind Extensive Cyberattacks',
         url='https://sunrise-otter-ad6.notion.site/Japan-Uncovers-Chinese-Hacker-Behind-Extensive-Cyberattacks-1788e85494cf805ea7b1fefbeea08098'),
    dict(key='breach', cat='Data Breach', date='2024-02-23', min=6, img='blog3', alt='Cuidado! Criminosos Estão Usando Seus Dados para Golpes', lang='pt',
         title='Cuidado! Criminosos Estão Usando Seus Dados para Golpes',
         url='https://sunrise-otter-ad6.notion.site/Cuidado-Criminosos-est-o-Usando-Seus-Dados-para-Golpes-fb3d132105e44bdda56c3c06cd7e94cc'),
    dict(key='crime', cat='Security Research', date='2023-10-11', min=8, img='blog2', alt='Explorando o Mundo do Crime Digital', lang='pt',
         title='Explorando o Mundo do Crime Digital',
         url='https://sunrise-otter-ad6.notion.site/Explorando-o-Mundo-do-Crime-com-a-Sociedade-An-nima-S-A-33af64221fa24ba098093c9b0989f64a'),
    dict(key='social', cat='Social Engineering', date='2023-06-21', min=4, img='blog1', alt='O Perigo da Engenharia Social', lang='pt',
         title='O Perigo da Engenharia Social: Principais Ataques e Como se Proteger',
         url='https://sunrise-otter-ad6.notion.site/O-Perigo-da-Engenharia-Social-Principais-Ataques-e-Como-se-Proteger-209272682c174545b7cbecba58704435'),
]


# ---------------------------------------------------------------- partes comuns
def head(P, title_key, desc_key, extra=''):
    alts = '\n'.join(f'  <link rel="alternate" hreflang="{HTML_LANG[l]}" href="{P.url(l)}">' for l in LANGS)
    alts += f'\n  <link rel="alternate" hreflang="x-default" href="{P.url("pt")}">'
    og_alt = '\n'.join(f'  <meta property="og:locale:alternate" content="{LOCALE[l]}">' for l in LANGS if l != P.lang)
    title, desc = P.t(title_key), P.t(desc_key)
    return f'''<!DOCTYPE html>
<html lang="{HTML_LANG[P.lang]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Natanael Lima">
  <meta name="keywords" content="cybersecurity, red team, penetration testing, ethical hacker, RPA, automation">
  <meta name="theme-color" content="#000000">
  <link rel="canonical" href="{P.url()}">
{alts}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Natanael Lima">
  <meta property="og:locale" content="{LOCALE[P.lang]}">
{og_alt}
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{P.url()}">
  <meta property="og:image" content="{SITE}img/my-avatar.png">
  <meta name="twitter:card" content="summary">
  <link rel="icon" href="{P.asset('favicon.svg')}" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{P.asset('css/style.css')}">
  <script>document.documentElement.classList.add('js')</script>{extra}
</head>
<body>
{SPRITE}<a class="skip" href="#main">{P.t('skip')}</a>
'''


def lang_switch(P, cls='lang'):
    links = ''.join(
        f'<a href="{P.link_to_lang(l)}" hreflang="{HTML_LANG[l]}" lang="{HTML_LANG[l]}" title="{LANG_NAME[l]}"'
        + (' aria-current="true"' if l == P.lang else '') + f'>{l.upper()}</a>'
        for l in LANGS)
    return f'<div class="{cls}" role="group" aria-label="{P.t("lang_label")}">{links}</div>'


def nav(P):
    home = P.page == 'index'
    pre = '' if home else 'index.html'
    items = [
        ('home', '#hero' if home else 'index.html', 'hero'),
        ('about', pre + '#about', 'about'),
        ('skills', pre + '#skills', 'skills'),
        ('experience', pre + '#experience', 'experience'),
        ('projects', 'projects.html', 'projects'),
        ('blog', 'blog.html', 'blog'),
        ('contact', pre + '#contact', 'contact'),
    ]

    def link(key, href, sec, mobile=False):
        attrs = ''
        if home and href.startswith('#'):
            attrs += f' data-section="{sec}"'
        if P.page == sec:
            attrs += ' class="active" aria-current="page"'
        tail = i('right') if mobile else ''
        return f'<a href="{href}"{attrs}>{P.t(key)}{tail}</a>'

    desk = ''.join(link(*x) for x in items)
    mob = ''.join(link(*x, mobile=True) for x in items)
    brand_href = '#hero' if home else 'index.html'
    return f'''<header class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="{brand_href}" aria-label="{P.t('home_aria')}"><span class="brand-tile">NL</span><span class="brand-name">Natanael Lima<small>Red Team Specialist</small></span></a>
    <nav class="nav-links" aria-label="{P.t('nav_main')}">{desk}</nav>
    <div class="nav-side">
      {lang_switch(P)}
      <a class="btn btn-primary btn-sm btn-cta" href="{WA}" {EXT}>{i('whatsapp')} {P.t('cta')}</a>
      <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="mobileMenu" aria-label="{P.t('menu_open')}" data-label-open="{P.t('menu_open')}" data-label-close="{P.t('menu_close')}">{i('menu')}</button>
    </div>
  </div>
</header>
<nav class="mobile-menu" id="mobileMenu" aria-label="{P.t('nav_mobile')}">
  {mob}
  <a class="btn btn-primary" href="{WA}" {EXT}>{i('whatsapp')} {P.t('cta')}</a>
</nav>
<main id="main">
'''


def footer(P):
    return f'''</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="index.html" aria-label="{P.t('home_aria')}"><span class="brand-tile">NL</span></a>
        <p>{P.t('f_about')}</p>
        {lang_switch(P, 'lang lang-footer')}
      </div>
      <div>
        <h4>{P.t('f_nav')}</h4>
        <ul><li><a href="index.html">{P.t('home')}</a></li><li><a href="index.html#about">{P.t('about')}</a></li><li><a href="index.html#skills">{P.t('skills')}</a></li><li><a href="index.html#experience">{P.t('experience')}</a></li><li><a href="blog.html">{P.t('blog')}</a></li></ul>
      </div>
      <div>
        <h4>{P.t('projects')}</h4>
        <ul>{''.join(f'<li><a href="projects.html#{p["id"]}">{pname(p, P.lang)}</a></li>' for p in PROJECTS)}<li><a href="projects.html">{P.t('f_all')}</a></li></ul>
      </div>
      <div>
        <h4>{P.t('contact')}</h4>
        <ul><li><a href="{WA}" {EXT}>+351 910 617 161</a></li><li><a href="{MAIL}">natanaellima65@gmail.com</a></li><li><a href="{CV}" {EXT}>{P.t('cv')}</a></li></ul>
      </div>
      <div>
        <h4>{P.t('f_social')}</h4>
        <ul><li><a href="{GH}" {EXT}>{i('github')} GitHub</a></li><li><a href="{LI}" {EXT}>{i('linkedin')} LinkedIn</a></li><li><a href="{WA}" {EXT}>{i('whatsapp')} WhatsApp</a></li></ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p><span class="hl">&lt;</span>2025<span class="hl">/&gt;</span> Natanael Lima • Red Team Specialist</p>
      <p><span class="hl">$</span> echo "Built with ♥ and code"</p>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" {EXT} aria-label="{P.t('wa_float')}">{i('whatsapp')}</a>
<script src="{P.asset('js/main.js')}" defer></script>
</body>
</html>
'''


def post_meta(P, p):
    bits = [f'<time datetime="{p["date"]}">{DATES[p["date"]][P.lang]}</time>', P.t('read_min').format(n=p['min'])]
    note = T['in_lang_' + p['lang']][P.lang]
    if note:
        bits.append(f'<span class="lang-note">{note}</span>')
    return ' · '.join(bits)


def post_card(P, p, with_ex=True):
    ex = f'<p>{POST_TX[p["key"]][P.lang]}</p>' if with_ex else ''
    return f'''<a class="card hover media-card post" data-cat="{p['cat']}" href="{p['url']}" {EXT} hreflang="{HTML_LANG[p['lang']]}">
        <span class="thumb"><img src="{P.asset('img/' + p['img'] + '.webp')}" alt="{p['alt']}" loading="lazy"><span class="label">{p['cat']}</span></span>
        <span class="body">
          <span class="meta">{post_meta(P, p)}</span>
          <h3 lang="{HTML_LANG[p['lang']]}">{p['title']}</h3>
          {ex}
          <span class="btn btn-primary btn-block">{P.t('more')}</span>
        </span>
      </a>'''


def contact_section(P):
    t = P.t
    return f'''<section class="section contact" id="contact">
  <div class="wrap contact-grid">
    <div class="contact-copy reveal">
      <h2>{t('contact_h')}</h2>
      <p>{t('contact_p')}</p>
      <div class="channels">
        <a class="channel" href="{WA}" {EXT}><span class="ico-tile">{i('whatsapp')}</span><span><b>{t('ch_wa')}</b><span>+351 910 617 161</span></span></a>
        <a class="channel" href="{MAIL}"><span class="ico-tile">{i('mail')}</span><span><b>{t('ch_mail')}</b><span>natanaellima65@gmail.com</span></span></a>
        <a class="channel" href="{LI}" {EXT}><span class="ico-tile">{i('linkedin')}</span><span><b>LinkedIn</b><span>linkedin.com/in/natanaellima10</span></span></a>
        <a class="channel" href="{GH}" {EXT}><span class="ico-tile">{i('github')}</span><span><b>GitHub</b><span>github.com/ademakin3051</span></span></a>
      </div>
    </div>
    <div class="card form-card reveal">
      <h3>{t('form_h')}</h3>
      <form class="form" id="contactForm" novalidate data-msg-missing="{t('f_missing')}" data-msg-opening="{t('f_opening')}" data-signature="{t('f_sig')}">
        <div class="field"><label for="f-name">{t('f_name')}</label><input id="f-name" name="name" type="text" placeholder="{t('f_name_ph')}" autocomplete="name"></div>
        <div class="field"><label for="f-email">{t('f_email')}<i>*</i></label><input id="f-email" name="email" type="email" placeholder="{t('f_email_ph')}" autocomplete="email" required></div>
        <div class="field full"><label for="f-subject">{t('f_subject')}<i>*</i></label><input id="f-subject" name="subject" type="text" placeholder="{t('f_subject_ph')}" required></div>
        <div class="field full"><label for="f-msg">{t('f_msg')}</label><textarea id="f-msg" name="message" placeholder="{t('f_msg_ph')}"></textarea></div>
        <div class="form-foot">
          <button class="btn btn-primary" type="submit">{i('send')} {t('f_send')}</button>
          <small id="formNote" aria-live="polite">{t('f_note')}</small>
        </div>
      </form>
    </div>
  </div>
</section>
'''


# ---------------------------------------------------------------- home
def index(lang):
    P = Page(lang, 'index')
    t = P.t
    ld = '\n  <script type="application/ld+json">\n  {"@context":"https://schema.org","@type":"Person","name":"Natanael Lima","jobTitle":"Red Team Specialist","url":"https://natanaellima.blog/","image":"https://natanaellima.blog/img/my-avatar.png","email":"mailto:natanaellima65@gmail.com","sameAs":["https://github.com/ademakin3051","https://www.linkedin.com/in/natanaellima10"],"knowsAbout":["Cybersecurity","Red Team","Penetration Testing","Ethical Hacking","RPA","Automação de Processos"]}\n  </script>'
    h = head(P, 'title_index', 'desc_index', ld)
    certs = [
        ('https://www.udemy.com/certificate/UC-26ec2d8b-86dd-4f1c-9417-3102b5f21b7a/', 'logo-1', 'Udemy', 'Ethical Hacking', 'Udemy'),
        ('https://desecsecurity.com/valida-certificado/LIJJ-QVKIR-SFUQ', 'logo-2', 'Desec', t('c_pentest'), 'Desec Security'),
        ('https://www.linkedin.com/learning/certificates/5a86355f50f3663fcb7aa8a48376c1d0caf460ae9632edbb9fa58a93d5b31c6b', 'logo-3', 'LinkedIn', 'Cybersecurity', 'LinkedIn Learning'),
        ('https://www.linkedin.com/learning/certificates/0dbd5d505aa8e0c468e11af12f145dfb0e1c47f28f5ca8c3efc71a8c6f935ca0', 'logo-4', 'LinkedIn', 'LGPD', 'LinkedIn Learning'),
        ('https://www.conquerplus.com.br/certificates/831c5500-523f-4704-9b66-84f8b34e093d?enrollment', 'logo-5', 'Conquer', 'Power BI', 'Conquer'),
        ('https://drive.google.com/file/d/1TB1oBiUGR-0H-Q0NRWL40U59t6-S4_BA/view', 'logo-6', 'Hackers Hive', 'Metasploit', 'Hackers Hive'),
    ]
    cert_html = '\n      '.join(f'<a class="cert" href="{u}" {EXT} title="{tt}"><img src="{P.asset("img/" + img + ".webp")}" alt="{alt}" width="92" height="92" loading="lazy"><span><b>{tt}</b><small>{by}</small></span></a>' for u, img, alt, tt, by in certs)
    people = [('depoimento1', 'Victor Bufalari'), ('depoimento2', 'Elisângela Bassete'), ('depoimento3', 'Jaqueline Monteiro'), ('depoimentos4', 'Michael Douglas')]
    quote_html = '\n      '.join(
        f'<figure class="card quote reveal"><blockquote>{QUOTES[k][lang]}</blockquote><figcaption><img src="{P.asset("img/" + img + ".webp")}" alt="{n}" width="48" height="48" loading="lazy"><span><b>{n}</b><small>{ROLES[k][lang]}</small></span></figcaption></figure>'
        for k, (img, n) in enumerate(people))
    proj_html = '\n      '.join(f'''<a class="card hover media-card reveal" href="projects.html#{p['id']}">
        <span class="thumb"><img src="{P.asset('img/' + p['img'] + '.webp')}" alt="{pname(p, lang)}" loading="lazy"><span class="status">{t('done')}</span><span class="label">{PROJ[p['id']]['cat'][lang]}</span></span>
        <span class="body">
          <span class="meta">PROJECT / {p['n']}</span>
          <h3>{pname(p, lang)}</h3>
          <p>{PROJ[p['id']]['short'][lang]}</p>
          <span class="tags">{''.join(f'<span class="tag">{tg}</span>' for tg in p['tags'][:4])}</span>
          <span class="btn btn-primary btn-block">{t('more')}</span>
        </span>
      </a>''' for p in PROJECTS)
    posts_html = '\n        '.join(post_card(P, p, with_ex=False) for p in POSTS)
    lvl = {3: t('lvl3'), 2: t('lvl2'), 1: t('lvl1')}
    domains = [('Cyber Security', 3), ('Computer Repair', 3), ('Networking', 2), (t('d_rpa'), 2), ('Python', 1)]
    dom_html = '\n        '.join(f'<li class="domain"><h4>{n}</h4><span class="level">{lvl[l]}<span class="pips" data-l="{l}"><i></i><i></i><i></i></span></span></li>' for n, l in domains)

    body = f'''
<section class="hero" id="hero" aria-label="Natanael Lima">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="hero-role">{t('role')}</p>
      <h1>Natanael <span>Lima</span></h1>
      <p class="hero-lead"><strong>{t('lead')}</strong></p>
      <div class="hero-cta">
        <a class="btn btn-primary btn-lg" href="{CV}" {EXT}>{i('doc')} {t('btn_cv')}</a>
        <a class="btn btn-light btn-lg" href="{GH}" {EXT}>{i('github')} {t('btn_gh')}</a>
        <a class="btn btn-ghost" href="projects.html">{i('layers')} {t('btn_projects')}</a>
        <a class="btn btn-ghost" href="#contact">{i('chat')} {t('btn_talk')}</a>
      </div>
      <div class="stats">
        <div class="stat"><strong>4+</strong><span>{t('stat_years')}</span></div>
        <div class="stat"><strong>10+</strong><span>{t('stat_projects')}</span></div>
        <div class="stat"><strong>16+</strong><span>{t('stat_certs')}</span></div>
      </div>
    </div>

    <div class="console">
      <div class="term" id="heroTerm" role="img" aria-label="{t('term_aria')}">
        <div class="term-bar"><span class="dots"><i></i><i></i><i></i></span><span class="title">natanael@security: ~</span></div>
        <div class="term-body" aria-hidden="true" lang="en">
          <div data-line><span class="prompt">natanael@security<b>:~$</b></span> <span class="cmd" data-text="whoami">whoami</span></div>
          <div data-line><br><span class="term-out" style="font-weight:500">Natanael Lima</span></div>
          <div data-line><span class="term-dim">Cyber Security</span></div>
          <div data-line><span class="term-dim">Automation</span></div>
          <div data-line><span class="term-dim">Technology</span><br><br></div>
          <div data-line><span class="prompt">natanael@security<b>:~$</b></span> <span class="cmd" data-text="echo $ROLE">echo $ROLE</span></div>
          <div data-line><span class="term-out" id="typingText"></span><span class="cursor"></span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="wrap">
    <header class="head reveal">
      <h2>{t('about_h')}</h2>
      <p>{t('about_sub')}</p>
    </header>
    <div class="about-grid">
      <aside class="card id-card reveal">
        <div class="id-photo"><img src="{P.asset('img/my-avatar.webp')}" alt="Natanael Lima - Red Team Specialist" loading="lazy"></div>
        <h3>Natanael Lima</h3>
        <p>Red Team Specialist</p>
      </aside>
      <div class="about-copy reveal">
        <div class="bio">
          <p>{t('bio1')}</p>
          <p>{t('bio2')}</p>
          <p>{t('bio3')}</p>
        </div>
        <dl class="spec">
          <div><dt>{t('k_name')}</dt><dd>Natanael Evangelista</dd></div>
          <div><dt>{t('k_exp')}</dt><dd>{t('v_exp')}</dd></div>
          <div><dt>{t('k_spec')}</dt><dd>Pentesting &amp; Red Team Operations<small>Desec Security</small></dd></div>
          <div><dt>{t('k_study')}</dt><dd>{t('degree')}<small>{t('uni_now')}</small></dd></div>
        </dl>
        <div>
          <p class="subhead">{t('areas')}</p>
          <div class="areas">
            <div class="card hover area"><span class="ico-tile">{i('terminal')}</span><span><h4>Ethical Hacking</h4><p>Red Team &amp; Penetration Testing</p></span></div>
            <div class="card hover area"><span class="ico-tile">{i('cog')}</span><span><h4>RPA</h4><p>{t('a_rpa')}</p></span></div>
            <div class="card hover area"><span class="ico-tile">{i('headset')}</span><span><h4>{t('a_support')}</h4><p>{t('a_support_d')}</p></span></div>
            <div class="card hover area"><span class="ico-tile">{i('chip')}</span><span><h4>Hardware</h4><p>{t('a_hw_d')}</p></span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="skills">
  <div class="wrap">
    <header class="head reveal">
      <h2>{t('skills_h')}</h2>
      <p>{t('skills_sub')}</p>
    </header>
    <div class="skills-grid">
      <article class="card hover skill reveal"><div class="skill-top"><span class="ico-tile">{i('terminal')}</span><h3>Cyber Security<small>{t('s_sec')}</small></h3></div><div class="tags"><span class="tag on">Ethical Hacking</span><span class="tag on">Penetration Testing</span><span class="tag on">Red Team</span><span class="tag">Kali Linux</span><span class="tag">Metasploit</span><span class="tag">Burp Suite</span><span class="tag">Nmap</span><span class="tag">SQLMap</span><span class="tag">Wireshark</span></div></article>
      <article class="card hover skill reveal"><div class="skill-top"><span class="ico-tile">{i('flash')}</span><h3>Automation<small>{t('s_auto')}</small></h3></div><div class="tags"><span class="tag on">RPA</span><span class="tag on">Python</span><span class="tag on">N8N</span><span class="tag">OpenAI</span><span class="tag">WhatsApp API</span><span class="tag">Webhooks</span><span class="tag">Tkinter</span></div></article>
      <article class="card hover skill reveal"><div class="skill-top"><span class="ico-tile">{i('server')}</span><h3>Infrastructure<small>{t('s_infra')}</small></h3></div><div class="tags"><span class="tag on">Networking</span><span class="tag on">Active Directory</span><span class="tag">GLPI</span><span class="tag">Docker</span><span class="tag">Git</span><span class="tag">Moodle</span></div></article>
      <article class="card hover skill reveal"><div class="skill-top"><span class="ico-tile">{i('chip')}</span><h3>{t('s_sup_t')}<small>{t('s_sup')}</small></h3></div><div class="tags"><span class="tag">{t('a_support_d')}</span><span class="tag">{t('a_hw_d')}</span><span class="tag">Computer Repair</span></div></article>
    </div>
    <div class="card domains reveal">
      <ul>
        {dom_html}
      </ul>
    </div>
  </div>
</section>

<section class="section" id="certs">
  <div class="wrap">
    <header class="head reveal">
      <h2>{t('certs_h')}</h2>
    </header>
    <div class="certs reveal">
      {cert_html}
    </div>
  </div>
</section>

<section class="section" id="experience">
  <div class="wrap">
    <header class="head reveal">
      <h2>{t('xp_h')}</h2>
    </header>
    <div class="xp-grid">
      <div class="card xp reveal">
        <p class="subhead">{i('briefcase')} {t('xp_work')}</p>
        <ol class="timeline">
          <li class="tl-item"><span class="tl-when">2023 – 2024</span><h4>Acamef/Academia do Bancário</h4><p>{t('xp1')}</p></li>
          <li class="tl-item"><span class="tl-when">2022 – 2023</span><h4>Blend IT Consultoria</h4><p>{t('xp2')}</p></li>
          <li class="tl-item"><span class="tl-when">2021 – 2022</span><h4>Sete Ambiental Logística</h4><p>{t('xp3')}</p></li>
        </ol>
      </div>
      <div class="card xp reveal">
        <p class="subhead">{i('school')} {t('xp_edu')}</p>
        <ol class="timeline">
          <li class="tl-item now"><span class="tl-when">2025 – {t('now')}</span><h4>{t('uni')}</h4><p>{t('degree')}</p></li>
          <li class="tl-item"><span class="tl-when">2024 – 2025</span><h4>Desec Security</h4><p>Pentesting &amp; Red Team Operations</p></li>
          <li class="tl-item"><span class="tl-when">2020 – 2021</span><h4>Elaborata Informática</h4><p>{t('edu3')}</p></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="projects">
  <div class="wrap">
    <header class="head reveal">
      <h2>{t('proj_h')}</h2>
      <p>{t('proj_sub')}</p>
    </header>
    <div class="card-grid">
      {proj_html}
    </div>
    <div class="head reveal" style="margin:40px auto 0"><a class="btn btn-ghost" href="projects.html">{i('layers')} {t('all_projects')}</a></div>
  </div>
</section>

<section class="section" id="blog">
  <div class="wrap">
    <header class="head reveal">
      <h2>{t('blog_h')}</h2>
      <p>{t('blog_sub')}</p>
    </header>
    <div class="carousel reveal" data-carousel>
      <button class="car-btn prev" type="button" aria-label="{t('prev')}">{i('left')}</button>
      <div class="track" tabindex="0" aria-label="{t('posts_aria')}">
        {posts_html}
      </div>
      <button class="car-btn next" type="button" aria-label="{t('next')}">{i('right')}</button>
      <div class="car-dots" aria-hidden="true"></div>
    </div>
  </div>
</section>

<section class="section" id="testimonials">
  <div class="wrap">
    <header class="head reveal">
      <h2><span class="hl">{t('rec_h')}</span></h2>
      <p>{t('rec_sub')}</p>
    </header>
    <div class="quotes">
      {quote_html}
    </div>
  </div>
</section>

<hr class="sep-line">
{contact_section(P)}'''
    return h + nav(P) + body + footer(P)


# ---------------------------------------------------------------- projetos
def projects(lang):
    P = Page(lang, 'projects')
    t = P.t
    h = head(P, 'title_projects', 'desc_projects')
    cases = '\n      '.join(f'''<article class="card case reveal" id="{p['id']}">
        <div class="case-media">
          <img src="{P.asset('img/' + p['img'] + '.webp')}" alt="{pname(p, lang)}" loading="lazy">
          <span class="status">{t('done')}</span>
        </div>
        <div class="case-body">
          <div class="case-id"><span>PROJECT / {p['n']}</span><b>{PROJ[p['id']]['cat'][lang]}</b></div>
          <h2>{pname(p, lang)}</h2>
          <p class="case-desc">{PROJ[p['id']]['desc'][lang]}</p>
          <p class="case-summary">{PROJ[p['id']]['short'][lang]}</p>
          <dl class="ps">
            <div><dt>{t('problem')}</dt><dd>{PROJ[p['id']]['prob'][lang]}</dd></div>
            <div><dt>{t('solution')}</dt><dd>{PROJ[p['id']]['sol'][lang]}</dd></div>
          </dl>
          <div class="tags">{''.join(f'<span class="tag">{tg}</span>' for tg in p['tags'])}</div>
          <div class="case-actions">
            <a class="btn btn-primary" href="{p['gh']}" {EXT}>{i('github')} {t('code')}</a>
            <a class="btn btn-ghost" href="{p['demo']}" {EXT}>{i('play')} {t('demo')}</a>
          </div>
        </div>
      </article>''' for p in PROJECTS)
    roads = [
        ('bug', 'is-dev', t('in_dev'), t('r1_name'), t('r1'), ['Python', 'Bash Script', t('r1_tag')]),
        ('wifi', 'is-plan', t('planned'), 'Network Monitor', t('r2'), ['Python', 'Scapy', 'Dashboard']),
        ('fish', 'is-plan', t('planned'), 'Phishing Detector', t('r3'), ['Python', 'ML', 'Browser Ext']),
    ]
    road_html = '\n      '.join(f'''<article class="card hover road reveal">
        <div class="road-top"><span class="ico-tile">{i(ic)}</span><span class="status {cls}">{st}</span></div>
        <h3>{nm}</h3>
        <p>{d}</p>
        <div class="tags">{''.join(f'<span class="tag">{tg}</span>' for tg in tags)}</div>
      </article>''' for ic, cls, st, nm, d, tags in roads)
    body = f'''
<section class="page-head">
  <div class="wrap">
    <span class="kicker">{t('kicker_proj')}</span>
    <h1>{t('proj_h1')}</h1>
    <p>{t('proj_sub_strong')}</p>
  </div>
</section>

<section class="section" id="todos">
  <div class="wrap">
    <div class="toolbar">
      <span class="count">{t('count')}</span>
      <div class="view-toggle" role="group" aria-label="{t('view_aria')}">
        <button type="button" data-view="full" aria-pressed="true">{i('layers')} {t('view_full')}</button>
        <button type="button" data-view="compact" aria-pressed="false">{i('code')} {t('view_all')}</button>
      </div>
    </div>
    <div class="cases" id="cases">
      {cases}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <header class="head reveal">
      <h2>{t('next_h')}</h2>
    </header>
    <div class="card-grid">
      {road_html}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap proj-stats">
    <div class="term reveal">
      <div class="term-bar"><span class="dots"><i></i><i></i><i></i></span><span class="title">~/projects/stats.sh</span></div>
      <div class="term-body">
        <p><span class="prompt">$</span> cat project_stats.json</p>
        <div class="kv">
          <div><strong>3</strong><span>{t('st_done')}</span></div>
          <div><strong>1</strong><span>{t('st_dev')}</span></div>
          <div><strong>2</strong><span>{t('st_plan')}</span></div>
          <div><strong>100%</strong><span>Open Source</span></div>
        </div>
        <p><span class="prompt">$</span> <span class="cursor"></span></p>
      </div>
    </div>
    <div class="card gh-cta reveal">
      <span class="ico-tile">{i('github')}</span>
      <h3>{t('gh_all')}</h3>
      <a class="btn btn-primary" href="{GH}" {EXT}>{i('github')} {t('gh_btn')}</a>
    </div>
  </div>
</section>
'''
    return h + nav(P) + body + footer(P)


# ---------------------------------------------------------------- blog
def blog(lang):
    P = Page(lang, 'blog')
    t = P.t
    h = head(P, 'title_blog', 'desc_blog')
    f = POSTS[0]
    cats = [p['cat'] for p in POSTS]
    filt = f'<button type="button" data-filter="all" aria-pressed="true">{t("all")}<sup>{len(POSTS)}</sup></button>' + ''.join(
        f'<button type="button" data-filter="{c}" aria-pressed="false">{c}<sup>{cats.count(c)}</sup></button>' for c in sorted(set(cats)))
    grid = '\n      '.join(post_card(P, p) for p in POSTS)
    note = T['in_lang_' + f['lang']][lang]
    note_html = f'<span class="lang-note">{note}</span>' if note else ''
    body = f'''
<section class="page-head">
  <div class="wrap">
    <span class="kicker">{t('kicker_blog')}</span>
    <h1>{t('blog_h1')}</h1>
    <p>{t('blog_sub_strong')}</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <a class="card hover feature reveal" href="{f['url']}" {EXT} hreflang="{HTML_LANG[f['lang']]}">
      <span class="feature-media"><img src="{P.asset('img/' + f['img'] + '.webp')}" alt="{f['alt']}"><span class="status">{t('featured')}</span></span>
      <span class="feature-body">
        <span class="meta"><span class="cat">{f['cat']}</span><span>{i('calendar')} <time datetime="{f['date']}">{DATES[f['date']][lang]}</time></span><span>{i('time')} {t('read_min').format(n=f['min'])}</span>{note_html}</span>
        <h2 lang="{HTML_LANG[f['lang']]}">{f['title']}</h2>
        <p>{POST_TX[f['key']][lang]}</p>
        <span class="btn btn-primary">{t('read_full')} {i('arrow')}</span>
      </span>
    </a>
  </div>
</section>

<section class="section" id="artigos">
  <div class="wrap">
    <header class="head reveal">
      <h2>{t('all_articles')}</h2>
    </header>
    <div class="filters reveal" role="group" aria-label="{t('filter_aria')}">{filt}</div>
    <div class="card-grid four">
      {grid}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="card cta-band reveal">
      <span class="ico-tile">{i('shield')}</span>
      <div>
        <h2>{t('protect_h')}</h2>
        <p>{t('protect_p')}</p>
      </div>
      <div class="actions">
        <a class="btn btn-primary" href="{LI}" {EXT}>{i('linkedin')} {t('follow_li')}</a>
        <a class="btn btn-ghost" href="index.html#contact">{i('chat')} {t('get_touch')}</a>
      </div>
    </div>
    <div style="margin-top:64px" class="reveal">
      <header class="head"><h2 style="font-size:clamp(1.6rem,3vw,2.2rem)"><span class="hl">{t('topics')}</span></h2></header>
      <div class="topics">
        <span class="tag">#CyberSecurity</span><span class="tag">#SocialEngineering</span><span class="tag">#DataBreach</span><span class="tag">#EthicalHacking</span><span class="tag">#RedTeam</span><span class="tag">#OSINT</span>
      </div>
    </div>
  </div>
</section>
'''
    return h + nav(P) + body + footer(P)


for lang in LANGS:
    d = os.path.join(OUT, DIR[lang])
    os.makedirs(d, exist_ok=True)
    for name, fn in [('index', index), ('projects', projects), ('blog', blog)]:
        open(os.path.join(d, f'{name}.html'), 'w').write(fn(lang))
print('ok')
