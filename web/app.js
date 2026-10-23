const installButton = document.getElementById('installButton');
const statusText = document.getElementById('statusText');
const modeBadge = document.getElementById('modeBadge');
const composerForm = document.getElementById('composerForm');
const promptInput = document.getElementById('promptInput');
const messages = document.getElementById('messages');
const quickPromptBtn = document.getElementById('quickPromptBtn');
const simulateBtn = document.getElementById('simulateBtn');
const holoScene = document.querySelector('.hologram-visual');

let deferredPrompt = null;

function setStatus(text, tone = 'normal') {
  statusText.textContent = text;
  const map = {
    normal: '#7cf0b7',
    warn: '#ffd166',
    success: '#7cf0b7'
  };

  const dot = document.querySelector('.live-dot');
  if (dot) {
    dot.style.background = map[tone] || map.normal;
    dot.style.boxShadow = `0 0 0 6px ${tone === 'warn' ? 'rgba(255,209,102,0.12)' : 'rgba(124,240,183,0.12)'}`;
  }
}

function updateMode() {
  const standalone = window.matchMedia('(display-mode: standalone)').matches;
  modeBadge.textContent = standalone ? 'Installed' : 'Browser';
}

function appendMessage(content, isUser = false) {
  const message = document.createElement('div');
  message.className = `message ${isUser ? 'user' : 'bot'}`;

  const p = document.createElement('p');
  p.textContent = content;
  message.appendChild(p);
  messages.appendChild(message);
  messages.scrollTop = messages.scrollHeight;
}

function generateReply(input) {
  const text = input.trim();

  if (!text) {
    return 'Please ask a valid question.';
  }

  const lower = text.toLowerCase();

  if (lower.includes('install') || lower.includes('package')) {
    return 'I can package this as a PWA for browser install, or prepare a Capacitor wrapper for Android APK build.';
  }

  if (lower.includes('code') || lower.includes('build')) {
    return 'The app is structured for a clean installable web shell. Next step can be a full AI dashboard, release packaging, or Android APK conversion.';
  }

  if (lower.includes('voice') || lower.includes('audio')) {
    return 'Voice workflow is ready for integration with speech-to-text and TTS, while keeping the app installable in browser mode.';
  }

  if (lower.includes('hologram') || lower.includes('3d') || lower.includes('visual')) {
    return 'The hologram layer is active: layered rings, scan-grid motion, floating particles, and live AI status overlays are already configured for the futuristic VHOTIEX interface.';
  }

  return `I’m processing: "${text}". The app is ready for installable PWA packaging, and can be extended with a full AI agent workflow or Android APK release.`;
}

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

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./service-worker.js').catch((error) => {
      console.error('Service worker registration failed:', error);
      setStatus('Offline support unavailable', 'warn');
    });
  });
}

window.addEventListener('beforeinstallprompt', (event) => {
  event.preventDefault();
  deferredPrompt = event;
  installButton.classList.remove('hidden');
  setStatus('Install available', 'success');
});

window.addEventListener('appinstalled', () => {
  setStatus('Installed successfully', 'success');
  updateMode();
  installButton.classList.add('hidden');
  deferredPrompt = null;
});

installButton.addEventListener('click', async () => {
  if (!deferredPrompt) {
    setStatus('Install prompt not ready', 'warn');
    return;
  }

  deferredPrompt.prompt();
  const choice = await deferredPrompt.userChoice;

  if (choice.outcome === 'accepted') {
    setStatus('Installation accepted', 'success');
  } else {
    setStatus('Install dismissed', 'warn');
  }

  deferredPrompt = null;
  installButton.classList.add('hidden');
});

composerForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const value = promptInput.value.trim();

  if (!value) return;

  appendMessage(value, true);
  promptInput.value = '';
  setStatus('Processing request', 'normal');

  setTimeout(() => {
    appendMessage(generateReply(value), false);
    setStatus('AI ready', 'success');
  }, 600);
});

quickPromptBtn.addEventListener('click', () => {
  promptInput.value = 'Create an installable AI app package with hologram visuals';
  promptInput.focus();
  setStatus('Quick launch ready', 'success');
});

simulateBtn.addEventListener('click', () => {
  appendMessage('Run demo workflow and package app experience.', true);
  setTimeout(() => {
    appendMessage('Demo complete. PWA install flow is active and the hologram interface is ready for deployment.', false);
    setStatus('Demo complete', 'success');
  }, 500);
});

setupHologramScene();
updateMode();
