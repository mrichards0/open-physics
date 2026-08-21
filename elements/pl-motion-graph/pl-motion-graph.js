(function () {
  document.querySelectorAll('.sf-motion-graph').forEach(function (graph) {
    var svg = graph.querySelector('svg');
    var cursor = graph.querySelector('.sf-cursor');
    var dot = graph.querySelector('.sf-cursor-dot');
    var reading = graph.querySelector('.sf-graph-reading');
    var vi = Number(graph.dataset.vi);
    var vf = Number(graph.dataset.vf);
    var duration = Number(graph.dataset.duration);
    function inspect(event) {
      var bounds = svg.getBoundingClientRect();
      var fraction = Math.max(0, Math.min(1, (event.clientX - bounds.left) / bounds.width));
      var x = 82 + 316 * fraction;
      var t = duration * fraction;
      var velocity = vi + (vf - vi) * fraction;
      var line = graph.querySelector('.sf-velocity-line');
      var y1 = Number(line.getAttribute('y1'));
      var y2 = Number(line.getAttribute('y2'));
      var y = y1 + (y2 - y1) * fraction;
      cursor.setAttribute('x1', x); cursor.setAttribute('x2', x);
      dot.setAttribute('cx', x); dot.setAttribute('cy', y);
      reading.textContent = 'At t = ' + t.toFixed(2) + ' s, v = ' + velocity.toFixed(2) + ' m/s.';
    }
    svg.addEventListener('pointermove', inspect);
  });
})();
