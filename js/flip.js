'use strict';

const flipCard = document.getElementById('flipCard');
const flipBtn = document.getElementById('flipToggleBtn');
const flipBackBtn = document.getElementById('flipBackBtn');
const ring = document.querySelector('.progress-ring__circle');

const DURATION = 850;
const RADIUS = 28;
const CIRC = 2 * Math.PI * RADIUS;

ring.style.strokeDasharray = CIRC;
ring.style.strokeDashoffset = CIRC;

let start = null;
let animating = false;

function animate(now) {
  if (!start) start = now;
  const elapsed = now - start;
  const pct = Math.min(elapsed / DURATION, 1);
  ring.style.strokeDashoffset = CIRC * (1 - pct);

  if (pct < 1) {
    requestAnimationFrame(animate);
  } else {
    flip();
  }
}

function flip() {
  flipCard.classList.add('flipped');
  start = null;
  animating = false;
  ring.style.strokeDashoffset = CIRC;
}

flipBtn.addEventListener('pointerenter', () => {
  if (animating) return;
  animating = true;
  requestAnimationFrame(animate);
});

flipBtn.addEventListener('pointerleave', () => {
  animating = false;
  start = null;
  ring.style.strokeDashoffset = CIRC;
});

flipBackBtn.addEventListener('click', () => {
  flipCard.classList.remove('flipped');
});
