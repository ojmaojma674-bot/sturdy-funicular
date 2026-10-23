const installButton = document.getElementById('installButton');
const statusText = document.getElementById('statusText');
const modeBadge = document.getElementById('modeBadge');
const composerForm = document.getElementById('composerForm');
const promptInput = document.getElementById('promptInput');
const messages = document.getElementById('messages');
const quickPromptBtn = document.getElementById('quickPromptBtn');
const simulateBtn = document.getElementById('simulateBtn');

let deferredPrompt = null;

function setStatus(text, tone = 'normal') {
  statusText.textContent = text;
  const map = {
    normal: '#7cf0b7',
    warn: '#ffd166',
    success: '#7cf0b7'
  };

  const dot = document.querySelector('.live-dot');
  dot.style.background = map[tone] || map.normal;
  dot.style.boxShadow = `0 0 0 6px ${tone === 'warn' ? 'rgba(255,209,102,0.12)' : 'rgba(124,240,183,0.12)'}`;
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

  return `I’m processing: "${text}". The app is ready for installable PWA packaging, and can be extended with a full AI agent workflow or Android APK release.';
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
  promptInput.value = 'Create an installable AI app package';
  promptInput.focus();
  setStatus('Quick launch ready', 'success');
});

simulateBtn.addEventListener('click', () => {
  appendMessage('Run demo workflow and package app experience.', true);
  setTimeout(() => {
    appendMessage('Demo complete. PWA install flow is active and the app is ready for browser deployment.', false);
    setStatus('Demo complete', 'success');
  }, 500);
});

updateMode();
