const installButton = document.getElementById('installButton');
const statusText = document.getElementById('statusText');
const modeText = document.getElementById('modeText');

let deferredPrompt = null;

function updateStatus(text) {
  statusText.textContent = text;
}

function updateMode() {
  const standalone = window.matchMedia('(display-mode: standalone)').matches;
  modeText.textContent = standalone ? 'Installed' : 'Browser';
}

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./service-worker.js').catch((error) => {
      console.error('Service worker registration failed:', error);
      updateStatus('Offline support unavailable');
    });
  });
}

window.addEventListener('beforeinstallprompt', (event) => {
  event.preventDefault();
  deferredPrompt = event;
  installButton.hidden = false;
  updateStatus('Install available');
});

window.addEventListener('appinstalled', () => {
  updateStatus('Installed successfully');
  updateMode();
  installButton.hidden = true;
  deferredPrompt = null;
});

installButton.addEventListener('click', async () => {
  if (!deferredPrompt) {
    updateStatus('Install prompt not ready');
    return;
  }

  deferredPrompt.prompt();
  const choice = await deferredPrompt.userChoice;

  if (choice.outcome === 'accepted') {
    updateStatus('Installation accepted');
  } else {
    updateStatus('Install dismissed');
  }

  deferredPrompt = null;
  installButton.hidden = true;
});

updateMode();
