var dropZone = document.getElementById('drop-zone');

dropZone.addEventListener('dragover', function (e) {
  e.stopPropagation();
  e.preventDefault();
  this.style.background = '#e1e7f0';
}, false);

dropZone.addEventListener('dragleave', function(e) {
  e.stopPropagation();
  e.preventDefault();
  this.style.background = '#ffffff';
}, false);

dropZone.addEventListener('drop', function(e) {
  e.stopPropagation();
  e.preventDefault();
  this.style.background = '#ffffff'; //背景色を白に戻す
  var files = e.dataTransfer.files; //ドロップしたファイルを取得
  fileInput.files = files; //inputのvalueをドラッグしたファイルに置き換える。
  previewFile(files[0]);
}, false);