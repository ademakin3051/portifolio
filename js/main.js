/* ==========================================================================
   Natanael Lima — Cyber Security Portfolio
   Shared behaviour: navigation, reveal-on-scroll, terminal typing,
   role typing, project index toggle and blog filters.
   ========================================================================== */
(function () {
    'use strict';

    const root = document.documentElement;
    root.classList.remove('no-js');
    root.classList.add('js');

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

    /* ---------------------------------------------------------------
       Navigation: scrolled state + mobile menu
       --------------------------------------------------------------- */
    const nav = document.querySelector('[data-nav]');
    const toggle = document.querySelector('[data-nav-toggle]');
    const mobileMenu = document.getElementById('mobileMenu');

    if (nav) {
        const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 12);
        onScroll();
        window.addEventListener('scroll', onScroll, { passive: true });
    }

    function setMenu(open) {
        if (!nav || !toggle) return;
        nav.classList.toggle('is-open', open);
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
        document.body.style.overflow = open ? 'hidden' : '';
    }

    if (toggle && mobileMenu) {
        toggle.addEventListener('click', () => setMenu(!nav.classList.contains('is-open')));
        mobileMenu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
        window.addEventListener('resize', () => { if (window.innerWidth > 960) setMenu(false); });
    }

    /* ---------------------------------------------------------------
       Active nav link for in-page sections (home page)
       --------------------------------------------------------------- */
    const sectionLinks = document.querySelectorAll('[data-section-link]');
    if (sectionLinks.length && 'IntersectionObserver' in window) {
        const byId = {};
        sectionLinks.forEach((link) => {
            const id = link.getAttribute('data-section-link');
            (byId[id] = byId[id] || []).push(link);
        });

        const spy = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                sectionLinks.forEach((l) => { l.classList.remove('is-active'); l.removeAttribute('aria-current'); });
                (byId[entry.target.id] || []).forEach((l) => { l.classList.add('is-active'); l.setAttribute('aria-current', 'location'); });
            });
        }, { rootMargin: '-45% 0px -50% 0px' });

        Object.keys(byId).forEach((id) => {
            const section = document.getElementById(id);
            if (section) spy.observe(section);
        });
    }

    /* ---------------------------------------------------------------
       Reveal on scroll
       --------------------------------------------------------------- */
    const revealEls = document.querySelectorAll('.reveal');
    if (!reduceMotion && 'IntersectionObserver' in window) {
        const io = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    io.unobserve(entry.target);
                }
            });
        }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
        revealEls.forEach((el) => io.observe(el));
    } else {
        revealEls.forEach((el) => el.classList.add('is-visible'));
    }

    /* ---------------------------------------------------------------
       Hero terminal: types commands, then prints their output.
       The full content is already in the HTML (works without JS).
       --------------------------------------------------------------- */
    const term = document.querySelector('[data-terminal]');
    if (term && !reduceMotion) {
        const lines = Array.from(term.querySelectorAll('.line'));
        const cmds = lines.map((line) => {
            const cmd = line.querySelector('.cmd');
            const text = cmd ? cmd.textContent : null;
            if (cmd) cmd.textContent = '';
            line.style.visibility = 'hidden';
            return { line, cmd, text };
        });

        (async function run() {
            await sleep(450);
            for (const item of cmds) {
                item.line.style.visibility = '';
                if (item.cmd) {
                    await sleep(260);
                    for (const ch of item.text) {
                        item.cmd.textContent += ch;
                        await sleep(38 + Math.random() * 45);
                    }
                    await sleep(240);
                } else {
                    await sleep(90);
                }
            }
        })();
    }

    /* ---------------------------------------------------------------
       Rotating role typing
       --------------------------------------------------------------- */
    const typing = document.getElementById('typingText');
    if (typing) {
        const phrases = (typing.getAttribute('data-phrases') || '').split('|').filter(Boolean);
        if (phrases.length) {
            if (reduceMotion) {
                typing.textContent = phrases[0];
            } else {
                let p = 0, c = 0, deleting = false;
                const tick = () => {
                    const word = phrases[p];
                    c += deleting ? -1 : 1;
                    typing.textContent = word.substring(0, c);
                    let delay = deleting ? 45 : 90;
                    if (!deleting && c === word.length) { delay = 2000; deleting = true; }
                    else if (deleting && c === 0) { deleting = false; p = (p + 1) % phrases.length; delay = 450; }
                    setTimeout(tick, delay);
                };
                setTimeout(tick, 1200);
            }
        }
    }

    /* ---------------------------------------------------------------
       Projects: expandable "Todos os Projetos" index
       --------------------------------------------------------------- */
    const expandBtn = document.getElementById('expandProjectsBtn');
    const expandPanel = document.getElementById('allProjectsContainer');
    if (expandBtn && expandPanel) {
        const label = document.getElementById('expandBtnText');
        expandBtn.addEventListener('click', () => {
            const open = expandBtn.getAttribute('aria-expanded') !== 'true';
            expandBtn.setAttribute('aria-expanded', String(open));
            expandPanel.classList.toggle('is-open', open);
            expandPanel.setAttribute('aria-hidden', String(!open));
            if ('inert' in expandPanel) expandPanel.inert = !open;
            if (label) label.textContent = open ? 'Ocultar Projetos' : 'Ver Todos os Projetos';
            if (open) {
                setTimeout(() => expandPanel.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' }), 300);
            }
        });
    }

    /* ---------------------------------------------------------------
       Blog: category filters
       --------------------------------------------------------------- */
    const filters = document.querySelectorAll('[data-filter]');
    const posts = document.querySelectorAll('[data-category]');
    if (filters.length && posts.length) {
        const empty = document.getElementById('postsEmpty');
        filters.forEach((btn) => {
            const key = btn.getAttribute('data-filter');
            const count = key === 'all' ? posts.length : document.querySelectorAll(`[data-category~="${key}"]`).length;
            const badge = btn.querySelector('.count');
            if (badge) badge.textContent = count;

            btn.addEventListener('click', () => {
                filters.forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
                let shown = 0;
                posts.forEach((post) => {
                    const match = key === 'all' || post.getAttribute('data-category').split(' ').includes(key);
                    post.hidden = !match;
                    if (match) { shown++; post.classList.add('is-visible'); }
                });
                if (empty) empty.hidden = shown !== 0;
            });
        });
    }
})();
