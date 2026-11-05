// Project page helpers (adapted from the Academic Project Page Template; no jQuery needed).
function toggleMoreWorks() {
  var dropdown = document.getElementById('moreWorksDropdown');
  var button = document.querySelector('.more-works-btn');
  if (!dropdown || !button) return;
  var open = dropdown.classList.toggle('show');
  button.classList.toggle('active', open);
}

document.addEventListener('click', function (event) {
  var container = document.querySelector('.more-works-container');
  var dropdown = document.getElementById('moreWorksDropdown');
  var button = document.querySelector('.more-works-btn');
  if (container && dropdown && !container.contains(event.target)) {
    dropdown.classList.remove('show');
    if (button) button.classList.remove('active');
  }
});

document.addEventListener('keydown', function (event) {
  if (event.key !== 'Escape') return;
  var dropdown = document.getElementById('moreWorksDropdown');
  var button = document.querySelector('.more-works-btn');
  if (dropdown) dropdown.classList.remove('show');
  if (button) button.classList.remove('active');
});

function copyBibTeX() {
  var el = document.getElementById('bibtex-code');
  var button = document.querySelector('.copy-bibtex-btn');
  if (!el || !button) return;
  var label = button.querySelector('.copy-text');
  var done = function () {
    button.classList.add('copied');
    label.textContent = 'Cop';
    setTimeout(function () {
      button.classList.remove('copied');
      label.textContent = 'Copy';
    }, 2000);
  };
  var fallback = function () {
    var ta = document.createElement('textarea');
    ta.value = el.textContent;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    done();
  };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(el.textContent).then(done).catch(fallback);
  } else {
    fallback();
  }
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

window.addEventListener('scroll', function () {
  var btn = document.querySelector('.scroll-to-top');
  if (!btn) return;
  btn.classList.toggle('visible', window.pageYOffset > 300);
});
