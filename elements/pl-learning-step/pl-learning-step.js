(function () {
  function initializeStep(step) {
    step.querySelectorAll('.sf-learning-hint').forEach(function (hint) {
      var input = hint.nextElementSibling;
      if (!input || input.tagName !== 'INPUT') return;
      hint.addEventListener('toggle', function () {
        if (hint.open) input.value = 'opened';
      });
    });
  }

  document.querySelectorAll('.sf-learning-step').forEach(initializeStep);
})();
