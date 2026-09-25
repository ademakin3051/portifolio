/* Natanael Lima — interações do site (sem dependências) */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Navbar: sombra ao rolar ---------- */
  var nav = document.querySelector('.nav');
  function onScroll() {
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 8);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Menu mobile ---------- */
  var menuBtn = document.getElementById('menuBtn');
  var mobileMenu = document.getElementById('mobileMenu');
  if (menuBtn && mobileMenu) {
    var setMenu = function (open) {
      mobileMenu.classList.toggle('open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      menuBtn.querySelector('use').setAttribute('href', open ? '#i-close' : '#i-menu');
    };
    menuBtn.addEventListener('click', function () {
      setMenu(!mobileMenu.classList.contains('open'));
    });
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { setMenu(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setMenu(false);
    });
  }

  /* ---------- Link ativo conforme a seção visível (home) ---------- */
  var sectionLinks = document.querySelectorAll('[data-section]');
  if (sectionLinks.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = entry.target.id;
        sectionLinks.forEach(function (a) {
          a.classList.toggle('active', a.getAttribute('data-section') === id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    document.querySelectorAll('main section[id]').forEach(function (s) { spy.observe(s); });
  }

  /* ---------- Revelação suave ao rolar ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if (!reduceMotion && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Terminal do hero ---------- */
  var term = document.getElementById('heroTerm');
  if (term) {
    var roles = ['Hardware Support', 'Penetration Tester', 'Ethical Hacker', 'System Support', 'RPA Developer'];
    var roleEl = document.getElementById('typingText');

    var cycleRoles = function () {
      if (!roleEl) return;
      if (reduceMotion) { roleEl.textContent = roles.join(' / '); return; }
      var i = 0, c = 0, del = false;
      (function tick() {
        var word = roles[i];
        c += del ? -1 : 1;
        roleEl.textContent = word.slice(0, c);
        var wait = del ? 45 : 90;
        if (!del && c === word.length) { wait = 1900; del = true; }
        else if (del && c === 0) { del = false; i = (i + 1) % roles.length; wait = 400; }
        setTimeout(tick, wait);
      })();
    };

    var lines = term.querySelectorAll('[data-line]');
    if (reduceMotion) {
      lines.forEach(function (l) { l.hidden = false; });
      cycleRoles();
    } else {
      lines.forEach(function (l) { l.hidden = true; });
      var typeCmd = function (el, done) {
        var target = el.querySelector('.cmd');
        var text = target ? target.getAttribute('data-text') : '';
        el.hidden = false;
        if (!target) { setTimeout(done, 90); return; }
        var n = 0;
        (function step() {
          target.textContent = text.slice(0, ++n);
          if (n < text.length) setTimeout(step, 55 + Math.random() * 45);
          else setTimeout(done, 260);
        })();
      };
      var idx = 0;
      var next = function () {
        if (idx >= lines.length) { cycleRoles(); return; }
        typeCmd(lines[idx++], next);
      };
      setTimeout(next, 700);
    }
  }

  /* ---------- Projetos: alternar visualização ---------- */
  var cases = document.getElementById('cases');
  var viewBtns = document.querySelectorAll('[data-view]');
  if (cases && viewBtns.length) {
    viewBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var compact = btn.getAttribute('data-view') === 'compact';
        cases.classList.toggle('compact', compact);
        viewBtns.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
      });
    });
  }

  /* ---------- Blog: filtro por categoria ---------- */
  var filterBtns = document.querySelectorAll('[data-filter]');
  var posts = document.querySelectorAll('.post[data-cat]');
  if (filterBtns.length && posts.length) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var cat = btn.getAttribute('data-filter');
        filterBtns.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
        posts.forEach(function (p) {
          p.hidden = !(cat === 'all' || p.getAttribute('data-cat') === cat);
        });
      });
    });
  }
})();
