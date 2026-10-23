const holoScene = document.querySelector('.hologram-visual');

function setupHologramScene() {
  if (!holoScene) {
    return;
  }

  for (let i = 0; i < 16; i += 1) {
    const particle = document.createElement('span');
    const size = 4 + Math.random() * 10;
    particle.className = 'holo-particle';
    particle.style.left = `${Math.random() * 100}%`;
    particle.style.top = `${Math.random() * 100}%`;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    particle.style.opacity = String(0.4 + Math.random() * 0.6);
    particle.style.animationDelay = `${(Math.random() * 4).toFixed(2)}s`;
    holoScene.appendChild(particle);
  }

  holoScene.addEventListener('pointermove', (event) => {
    const rect = holoScene.getBoundingClientRect();
    const px = (event.clientX - rect.left) / rect.width;
    const py = (event.clientY - rect.top) / rect.height;

    const rotateY = (px - 0.5) * 14;
    const rotateX = (0.5 - py) * 14;
    holoScene.style.setProperty('--tilt-x', `${rotateX.toFixed(2)}deg`);
    holoScene.style.setProperty('--tilt-y', `${rotateY.toFixed(2)}deg`);
  });

  holoScene.addEventListener('pointerleave', () => {
    holoScene.style.setProperty('--tilt-x', '0deg');
    holoScene.style.setProperty('--tilt-y', '0deg');
  });
}

setupHologramScene();
