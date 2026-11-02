(function(){
  var bar=document.getElementById('topbar'); if(!bar) return;
  var btn=bar.querySelector('.menu-btn'), panel=document.getElementById('mnav');
  function set(open){
    btn.setAttribute('aria-expanded',open?'true':'false');
    panel.hidden=!open; bar.classList.toggle('menu-open',open);
    document.documentElement.style.overflow=open?'hidden':'';
  }
  btn.addEventListener('click',function(){set(btn.getAttribute('aria-expanded')!=='true')});
  panel.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false)});
  window.matchMedia('(min-width:901px)').addEventListener('change',function(m){if(m.matches)set(false)});
  function onScroll(){bar.classList.toggle('is-scrolled',window.scrollY>40)}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
})();
