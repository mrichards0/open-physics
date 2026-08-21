(function () {
  document.querySelectorAll('.sf-motion-sim').forEach(function (sim) {
    var run = sim.querySelector('.sf-sim-run');
    var reset = sim.querySelector('.sf-sim-reset');
    var cart = sim.querySelector('.sf-sim-cart');
    var reading = sim.querySelector('.sf-sim-reading');
    var vi = Number(sim.dataset.vi), vf = Number(sim.dataset.vf);
    var duration = Number(sim.dataset.duration), distance = Number(sim.dataset.distance);
    var acceleration = (vf - vi) / duration;
    var animation = null;
    sim.querySelectorAll('input[type="radio"]').forEach(function (choice) {
      choice.addEventListener('change', function () { run.disabled = false; reading.textContent = 'Prediction saved. Run the simulation to observe the motion.'; });
    });
    function show(fraction) {
      var t = duration * fraction;
      var x = vi * t + 0.5 * acceleration * t * t;
      var position = distance === 0 ? fraction : x / distance;
      cart.style.left = (5 + 90 * Math.max(0, Math.min(1, position))) + '%';
      reading.textContent = 't = ' + t.toFixed(2) + ' s · v = ' + (vi + acceleration * t).toFixed(2) + ' m/s';
    }
    run.addEventListener('click', function () {
      if (animation) cancelAnimationFrame(animation);
      var start = performance.now(); run.disabled = true;
      function frame(now) {
        var fraction = Math.min(1, (now - start) / 3000);
        show(fraction);
        if (fraction < 1) animation = requestAnimationFrame(frame);
        else { animation = null; run.disabled = false; reading.textContent += ' · Observation complete.'; }
      }
      animation = requestAnimationFrame(frame);
    });
    reset.addEventListener('click', function () {
      if (animation) cancelAnimationFrame(animation); animation = null; show(0); run.disabled = !sim.querySelector('input[type="radio"]:checked');
    });
    show(0);
  });
})();
