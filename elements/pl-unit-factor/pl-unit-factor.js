(function () {
  document.querySelectorAll('.sf-unit-factor').forEach(function (factor) {
    var input = factor.querySelector('input[type="hidden"]');
    var slots = Array.from(factor.querySelectorAll('.sf-unit-slot'));
    var tokens = Array.from(factor.querySelectorAll('.sf-unit-token'));
    var status = factor.querySelector('.sf-unit-status');
    var selectedUnit = null;
    function values() { return slots.map(function (slot) { return slot.dataset.unit || ''; }); }
    function save() { input.value = JSON.stringify(values()); }
    function place(slot, unit) {
      slot.dataset.unit = unit;
      slot.textContent = unit;
      save();
      status.textContent = unit + ' placed in the ' + (slot.dataset.position === '0' ? 'numerator' : 'denominator') + '.';
    }
    var initial = [];
    try { initial = JSON.parse(input.value); } catch (_error) { initial = []; }
    slots.forEach(function (slot, index) { if (initial[index]) place(slot, initial[index]); });
    tokens.forEach(function (token) {
      token.addEventListener('click', function () {
        selectedUnit = token.dataset.unit;
        tokens.forEach(function (item) { item.setAttribute('aria-pressed', String(item === token)); });
        status.textContent = selectedUnit + ' selected. Choose a fraction box.';
      });
      token.addEventListener('dragstart', function (event) { event.dataTransfer.setData('text/plain', token.dataset.unit); });
    });
    slots.forEach(function (slot) {
      slot.addEventListener('click', function () { if (selectedUnit) place(slot, selectedUnit); });
      slot.addEventListener('dragover', function (event) { event.preventDefault(); slot.classList.add('sf-drag-over'); });
      slot.addEventListener('dragleave', function () { slot.classList.remove('sf-drag-over'); });
      slot.addEventListener('drop', function (event) {
        event.preventDefault(); slot.classList.remove('sf-drag-over');
        var unit = event.dataTransfer.getData('text/plain');
        if (tokens.some(function (token) { return token.dataset.unit === unit; })) place(slot, unit);
      });
    });
  });
})();
