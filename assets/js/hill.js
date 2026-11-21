/* 🔒 GÖRSEL KORUMA (Hilal Hanım): görsellerde sağ tık ve sürükleme kapalı — yalnız onun açık talimatıyla gevşetilir */
(function () {
  'use strict';
  function gorselMi(t) { return t && t.closest && t.closest('img, picture, video, .afis, .bolum-g, .durak, .bugun-g'); }
  document.addEventListener('contextmenu', function (e) { if (gorselMi(e.target)) e.preventDefault(); });
  document.addEventListener('dragstart', function (e) { if (gorselMi(e.target)) e.preventDefault(); });
})();
