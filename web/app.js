const state = { mode: 'idle', busy: false, agent: 'ORACLE' };
const root = document.getElementById('threeRoot');
const chatLog = document.getElementById('chatLog');
const chatForm = document.getElementById('chatForm');
const promptInput = document.getElementById('promptInput');
const agentSelect = document.getElementById('agentSelect');
const sendButton = document.getElementById('sendButton');
const voiceButton = document.getElementById('voiceButton');
const modeLabel = document.getElementById('modeLabel');
const coreState = document.getElementById('coreState');
const connectionLabel = document.getElementById('connectionLabel');
const activityValue = document.getElementById('activityValue');
const agentState = document.getElementById('agentState');
const voiceState = document.getElementById('voiceState');

let renderer, scene, camera, core, nodes, lines, clock;

const agentInstructions = {
  ORACLE: 'You are ORACLE, VHOTIEX general assistant. Be helpful, accurate, direct, and transparent about uncertainty.',
  NEXUS: 'You are NEXUS, VHOTIEX planning and research assistant. Structure research tasks, identify assumptions, distinguish verified facts from guesses. Do not claim live web browsing unless a browsing tool was actually used.',
  FORGE: 'You are FORGE, VHOTIEX coding specialist. Give maintainable code, exact file paths, explain tests, never claim code was executed if it was not.',
  SENTINEL: 'You are SENTINEL, VHOTIEX reviewer. Inspect risks, privacy, security, edge cases, and propose verifiable fixes. Do not execute actions.'
};

function setMode(mode) {
  state.mode = mode;
  if (modeLabel) modeLabel.textContent = mode.toUpperCase();
  if (coreState) coreState.textContent = mode.toUpperCase();
  if (connectionLabel) {
    connectionLabel.textContent = mode === 'thinking' ? 'PROCESSING' : mode === 'speaking' ? 'VOICE OUTPUT' : 'CORE STANDBY';
  }
  if (activityValue) {
    activityValue.textContent = mode === 'thinking' ? '87.4%' : mode === 'speaking' ? '64.2%' : '12.8%';
  }
  if (voiceState) {
    voiceState.textContent = mode === 'listening' ? 'LISTENING' : mode === 'speaking' ? 'SPEAKING' : 'STANDBY';
  }
  if (agentState) agentState.textContent = state.agent;
}

function addMessage(role, label, text) {
  const item = document.createElement('div');
  item.className = `message ${role}`;

  const tag = document.createElement('span');
  tag.className = 'message-tag';
  tag.textContent = label;

  const p = document.createElement('p');
  p.textContent = text;

  item.append(tag, p);
  chatLog.appendChild(item);
  chatLog.scrollTop = chatLog.scrollHeight;
}

function initScene() {
  if (!root || !window.THREE) return;

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(40, 1, 0.1, 100);
  camera.position.z = 7.2;

  renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.7));
  renderer.setSize(root.clientWidth || 500, root.clientHeight || 440);
  root.appendChild(renderer.domElement);

  const group = new THREE.Group();
  scene.add(group);

  const sphere = new THREE.SphereGeometry(1.22, 24, 18);
  const wire = new THREE.Mesh(
    sphere,
    new THREE.MeshBasicMaterial({ color: 0x168bff, wireframe: true, transparent: true, opacity: 0.26 })
  );
  group.add(wire);

  core = new THREE.Group();
  group.add(core);

  const positions = [];
  const count = 190;
  for (let i = 0; i < count; i++) {
    const y = 1 - (i / (count - 1)) * 2;
    const radius = Math.sqrt(1 - y * y);
    const angle = i * Math.PI * (3 - Math.sqrt(5));
    positions.push(Math.cos(angle) * radius * 1.18, y * 1.18, Math.sin(angle) * radius * 1.18);
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
  nodes = new THREE.Points(
    geo,
    new THREE.PointsMaterial({
      color: 0x8beaff,
      size: 0.045,
      transparent: true,
      opacity: 0.95,
      sizeAttenuation: true
    })
  );
  core.add(nodes);

  const linePositions = [];
  for (let i = 0; i < count; i++) {
    for (let j = i + 1; j < count; j++) {
      const dx = positions[i * 3] - positions[j * 3];
      const dy = positions[i * 3 + 1] - positions[j * 3 + 1];
      const dz = positions[i * 3 + 2] - positions[j * 3 + 2];
      if (dx * dx + dy * dy + dz * dz < 0.16 && Math.random() > 0.45) {
        linePositions.push(
          positions[i * 3], positions[i * 3 + 1], positions[i * 3 + 2],
          positions[j * 3], positions[j * 3 + 1], positions[j * 3 + 2]
        );
      }
    }
  }

  const lg = new THREE.BufferGeometry();
  lg.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
  lines = new THREE.LineSegments(
    lg,
    new THREE.LineBasicMaterial({ color: 0x29aaff, transparent: true, opacity: 0.28 })
  );
  core.add(lines);

  const glow = new THREE.Mesh(
    new THREE.SphereGeometry(0.7, 20, 16),
    new THREE.MeshBasicMaterial({ color: 0x1c7dff, transparent: true, opacity: 0.07 })
  );
  core.add(glow);

  scene.add(new THREE.AmbientLight(0xffffff, 1));
  clock = new THREE.Clock();
  animate();
  window.addEventListener('resize', resizeScene);
}

function resizeScene() {
  if (!renderer || !root || !root.clientWidth) return;
  camera.aspect = root.clientWidth / root.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(root.clientWidth, root.clientHeight);
}

function animate() {
  requestAnimationFrame(animate);
  const t = clock.getElapsedTime();

  if (core) {
    const speed = state.mode === 'thinking' ? 0.75 : state.mode === 'speaking' ? 0.5 : 0.18;
    core.rotation.y = t * speed;
    core.rotation.x = Math.sin(t * 0.25) * 0.16;
    const pulse = 1 + Math.sin(t * (state.mode === 'thinking' ? 5 : 1.6)) * (state.mode === 'thinking' ? 0.035 : 0.012);
    core.scale.setScalar(pulse);
    if (nodes && nodes.material) {
      nodes.material.color.set(state.mode === 'speaking' ? 0x9dffeb : state.mode === 'thinking' ? 0xff6d83 : 0x8beaff);
    }
  }

  if (renderer) renderer.render(scene, camera);
}

async function sendPrompt(prompt) {
  const text = prompt.trim();
  if (!text || state.busy) return;

  state.agent = agentSelect.value;
  if (agentState) agentState.textContent = state.agent;

  addMessage('user', 'YOU / COMMAND', text);
  promptInput.value = '';
  state.busy = true;
  sendButton.disabled = true;
  setMode('thinking');

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text, agent: state.agent, instruction: agentInstructions[state.agent] })
    });

    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.error || `Request failed (${response.status})`);

    addMessage('bot', `VHOTIEX / ${state.agent}`, data.reply || 'No text response returned.');
    setMode('speaking');
    speak(data.reply || '');
    setTimeout(() => {
      if (state.mode === 'speaking') setMode('idle');
    }, 1800);
  } catch (err) {
    addMessage('bot', 'SYSTEM / NOTICE', `${err.message}. Check the backend, API key, quota, and network connection.`);
    setMode('idle');
  } finally {
    state.busy = false;
    sendButton.disabled = false;
  }
}

function speak(text) {
  if (!('speechSynthesis' in window) || !text) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text.slice(0, 5000));
  utterance.lang = /[\u0600-\u06FF]/.test(text) ? 'ur-PK' : 'en-US';
  utterance.rate = 1;
  utterance.onstart = () => setMode('speaking');
  utterance.onend = () => setMode('idle');
  window.speechSynthesis.speak(utterance);
}

if (chatForm) {
  chatForm.addEventListener('submit', (event) => {
    event.preventDefault();
    sendPrompt(promptInput.value);
  });
}

if (promptInput) {
  promptInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      chatForm.requestSubmit();
    }
  });
}

if (agentSelect) {
  agentSelect.addEventListener('change', () => {
    state.agent = agentSelect.value;
    if (agentState) agentState.textContent = state.agent;
  });
}

document.querySelectorAll('[data-prompt]').forEach((button) => {
  button.addEventListener('click', () => {
    if (!promptInput) return;
    promptInput.value = button.dataset.prompt;
    promptInput.focus();
  });
});

if (voiceButton) {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  voiceButton.addEventListener('click', () => {
    if (!SpeechRecognition) {
      addMessage('bot', 'VOICE / NOTICE', 'Speech recognition is not supported in this browser. Try Chrome and check microphone permissions.');
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    recognition.onstart = () => setMode('listening');
    recognition.onresult = (event) => {
      if (promptInput) {
        promptInput.value = event.results[0][0].transcript;
        promptInput.focus();
      }
      setMode('idle');
    };
    recognition.onerror = () => setMode('idle');
    recognition.onend = () => {
      if (state.mode === 'listening') setMode('idle');
    };
    recognition.start();
  });
}

setMode('idle');
initScene();
