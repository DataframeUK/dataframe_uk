/* Dataframe — small progressive enhancements. The page works without this file. */
(function () {
  'use strict';

  // Mobile navigation
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (header && toggle && nav) {
    var setOpen = function (open) {
      header.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.querySelector('.visually-hidden').textContent = open ? 'Close menu' : 'Menu';
    };
    toggle.addEventListener('click', function () {
      setOpen(!header.classList.contains('is-open'));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && header.classList.contains('is-open')) {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  // Make whole rows of the services table clickable
  document.querySelectorAll('.df--nav tbody tr').forEach(function (row) {
    var link = row.querySelector('a');
    if (!link) return;
    row.addEventListener('click', function (e) {
      if (e.target.closest('a')) return;
      link.click();
    });
  });

  // Current year in the footer
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  // "Copy address" button, for visitors who use webmail rather than an email app
  var copyBtn = document.getElementById('copy-email');
  var copyStatus = document.getElementById('copy-status');
  if (copyBtn && copyStatus && navigator.clipboard && window.isSecureContext) {
    var resetTimer;
    copyBtn.hidden = false;
    copyBtn.addEventListener('click', function () {
      var address = copyBtn.getAttribute('data-copy');
      navigator.clipboard.writeText(address).then(function () {
        copyStatus.textContent = 'Copied to your clipboard.';
      }, function () {
        // Select the address so the visitor can copy it themselves
        var email = document.querySelector('.contact__email');
        if (email && window.getSelection) {
          var range = document.createRange();
          range.selectNodeContents(email);
          window.getSelection().removeAllRanges();
          window.getSelection().addRange(range);
        }
        copyStatus.textContent = 'Couldn’t copy automatically. The address is selected, so you can copy it.';
      });
      clearTimeout(resetTimer);
      resetTimer = setTimeout(function () { copyStatus.textContent = ''; }, 4000);
    });
  }
})();
