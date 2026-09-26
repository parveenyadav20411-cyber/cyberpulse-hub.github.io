<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CyberPulse AI - Voice Battle & Smart Advisor</title>
  <style>
    :root {
      --neon-green: #00ff88;
      --deep-bg: #030a06;
      --card-bg: rgba(6, 22, 13, 0.85);
      --red-alert: #ff0055;
    }
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Segoe UI', system-ui, sans-serif;
    }
    body {
      background-color: var(--deep-bg);
      color: #e0f2e9;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 15px;
      overflow-x: hidden;
      position: relative;
    }
    #matrixCanvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      pointer-events: none;
    }
    .web-shooter {
      position: absolute;
      pointer-events: none;
      z-index: 99;
      font-size: 2.2rem;
      transform: translate(-50%, -50%) scale(0);
      animation: shootWeb 0.6s cubic-bezier(0.1, 0.9, 0.2, 1) forwards;
      filter: drop-shadow(0 0 10px var(--neon-green));
    }
    @keyframes shootWeb {
      0% { transform: translate(-50%, -50%) scale(0.2); opacity: 1; }
      100% { transform: translate(-50%, -50%) scale(1.8) rotate(90deg); opacity: 0; }
    }
    .container {
      position: relative;
      z-index: 10;
      width: 100%;
      max-width: 480px;
      display: flex;
      flex-direction: column;
      gap: 15px;
      padding-bottom: 25px;
    }
    .brand-header {
      text-align: center;
      margin-top: 10px;
    }
    .brand-header h1 {
      font-size: 2rem;
      letter-spacing: 1.5px;
      color: var(--neon-green);
      text-shadow: 0 0 15px rgba(0, 255, 136, 0.5);
    }
    .brand-header p {
      font-size: 0.85rem;
      color: #799e8b;
    }
    .tab-bar {
      display: flex;
      gap: 10px;
      margin-top: 5px;
    }
    .tab-btn {
      flex: 1;
      padding: 10px;
      border: 1px solid var(--neon-green);
      background: rgba(0, 255, 136, 0.05);
      color: var(--neon-green);
      font-weight: 700;
      border-radius: 8px;
      cursor: pointer;
      transition: 0.3s;
    }
    .tab-btn.active {
      background: var(--neon-green);
      color: #031409;
      box-shadow: 0 0 15px rgba(0, 255, 136, 0.4);
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--neon-green);
      border-radius: 16px;
      padding: 18px;
      box-shadow: 0 0 20px rgba(0, 255, 136, 0.2);
      backdrop-filter: blur(8px);
      text-align: center;
    }
    .battle-meter-wrap {
      margin: 15px 0;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .fighter-bar-label {
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      font-weight: bold;
    }
    .progress-bar-bg {
      width: 100%;
      height: 22px;
      background: #092014;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid #1c5234;
      position: relative;
    }
    .progress-fill-user {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #00ff88, #00f2ff);
      box-shadow: 0 0 10px #00ff88;
      transition: width 0.1s linear;
    }
    .progress-fill-ai {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #ff0055, #ff7700);
      box-shadow: 0 0 10px #ff0055;
      transition: width 0.3s ease;
    }
    .shout-btn {
      width: 100%;
      padding: 14px;
      font-size: 1.05rem;
      font-weight: 800;
      border-radius: 10px;
      border: none;
      background: var(--neon-green);
      color: #04170c;
      cursor: pointer;
      margin-top: 10px;
      box-shadow: 0 0 15px rgba(0, 255, 136, 0.4);
      transition: 0.2s;
    }
    .shout-btn:active {
      transform: scale(0.97);
    }
    #chatResponse {
      min-height: 80px;
      background: rgba(0, 10, 5, 0.7);
      border-radius: 8px;
      padding: 12px;
      font-size: 0.9rem;
      line-height: 1.4;
      text-align: left;
      border-left: 3px solid var(--neon-green);
      margin: 15px 0;
      color: #c9f7df;
    }
    .input-group {
      display: flex;
      gap: 6px;
    }
    input[type="text"] {
      flex: 1;
      padding: 10px 12px;
      border-radius: 8px;
      border: 1px solid #1f402b;
      background: rgba(3, 15, 8, 0.8);
      color: #fff;
      font-size: 0.9rem;
      outline: none;
    }
    .hidden {
      display: none;
    }

    .creator-footer {
      background: rgba(4, 18, 10, 0.85);
      border: 1px dashed var(--neon-green);
      border-radius: 14px;
      padding: 16px;
      text-align: center;
      margin-top: 10px;
    }
    .creator-footer h3 {
      font-size: 1.05rem;
      color: var(--neon-green);
      margin-bottom: 6px;
    }
    .creator-footer p {
      font-size: 0.85rem;
      color: #9cb8a9;
      line-height: 1.4;
      margin-bottom: 12px;
    }
    .insta-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      border-radius: 25px;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.9rem;
      background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
      color: #fff;
      box-shadow: 0 0 15px rgba(220, 39, 67, 0.4);
      transition: 0.2s;
    }
    .support-note {
      font-size: 0.75rem;
      color: #638a74;
      margin-top: 10px;
    }
  </style>
</head>
<body>

  <canvas id="matrixCanvas"></canvas>

  <div class="container">
    <div class="brand-header">
      <h1>⚡ CYBERPULSE AI</h1>
      <p>Next-Gen Voice Battle & Intelligent Advisor</p>
    </div>

    <!-- Navigation Tabs -->
    <div class="tab-bar">
      <button class="tab-btn active" onclick="switchTab('battle')">⚔️ Voice Shout Battle</button>
      <button class="tab-btn" onclick="switchTab('advisor')">🤖 Deep Boy Advisor</button>
    </div>

    <!-- 1. Voice Shouting Game -->
    <div id="battleSection" class="card">
      <h2 style="color: var(--neon-green); font-size: 1.3rem;">SHOUT BATTLE ARENA</h2>
      <p style="font-size: 0.8rem; color: #8fa89b; margin-top: 4px;">
        Mic enable karke jitna zor se chilla sakte ho chillao! Dekhte hain tum jeette ho ya CyberPulse AI!
      </p>

      <div class="battle-meter-wrap">
        <div>
          <div class="fighter-bar-label">
            <span>🗣️ User Power (Voice Decibel)</span>
            <span id="userScoreText">0%</span>
          </div>
          <div class="progress-bar-bg">
            <div id="userBar" class="progress-fill-user"></div>
          </div>
        </div>

        <div>
          <div class="fighter-bar-label">
            <span style="color:#ff6688;">🤖 CyberPulse AI Roar</span>
            <span id="aiScoreText" style="color:#ff6688;">0%</span>
          </div>
          <div class="progress-bar-bg">
            <div id="aiBar" class="progress-fill-ai"></div>
          </div>
        </div>
      </div>

      <div id="battleStatus" style="font-weight: 700; min-height: 25px; color: #00f2ff;">
        Match start karo aur chilla kar meter 100% karo!
      </div>

      <button id="startShoutBtn" class="shout-btn" onclick="toggleShoutBattle()">
        🎙️ Start Shouting Match
      </button>
    </div>

    <!-- 2. AI Problem Solver -->
    <div id="advisorSection" class="card hidden">
      <h2 style="color: var(--neon-green); font-size: 1.3rem;">CyberPulse AI Advisor</h2>
      <p style="font-size: 0.8rem; color: #8fa89b;">Apni koi bhi pareshani likho, deep masculine voice me solution milega.</p>
      
      <div id="chatResponse">CyberPulse AI ready hai. Apni problem likhein, main seedha bolkar hal bataunga.</div>

      <div class="input-group">
        <input type="text" id="userInput" placeholder="Problem yahan likho..." onkeypress="if(event.key==='Enter') askAI()">
        <button class="tab-btn active" style="flex:0; padding:10px 15px;" onclick="askAI()">Batao</button>
      </div>
    </div>

    <!-- Creator Section -->
    <div class="creator-footer">
      <h3>Created & Developed by Parveen Yadav ⚡</h3>
      <p>Agar website achi lagi toh follow zaroor karein! Kuch problem aaye toh Instagram par DM karein.</p>
      
      <a href="https://instagram.com/parveen_yadav" target="_blank" class="insta-btn">
        📸 Follow on Instagram & DM
      </a>
      
      <div class="support-note">
        💡 24/7 Support: Koi dikkat aane par Instagram par DM karein, instant reply milega!
      </div>
    </div>
  </div>

  <script>
    // Screen Tap Spider Web Effect
    document.addEventListener('click', (e) => {
      if (['BUTTON', 'INPUT', 'A'].includes(e.target.tagName)) return;
      const web = document.createElement('div');
      web.className = 'web-shooter';
      web.innerText = '🕸️';
      web.style.left = e.clientX + 'px';
      web.style.top = e.clientY + 'px';
      document.body.appendChild(web);
      setTimeout(() => web.remove(), 600);
    });

    // Ambient Particles Matrix
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    let particles = [];
    function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    window.addEventListener('resize', resize);
    resize();
    for (let i = 0; i < 35; i++) {
      particles.push({ x: Math.random() * canvas.width, y: Math.random() * canvas.height, r: Math.random() * 2 + 1, s: Math.random() * 0.7 + 0.3 });
    }
    function renderBg() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = '#00ff88';
      particles.forEach(p => {
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
        p.y -= p.s; if (p.y < 0) p.y = canvas.height;
      });
      requestAnimationFrame(renderBg);
    }
    renderBg();

    // Deep Voice Speech Engine
    function speakDeep(text) {
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const utt = new SpeechSynthesisUtterance(text);
      utt.pitch = 0.6; 
      utt.rate = 1.0;
      const voices = window.speechSynthesis.getVoices();
      const deepV = voices.find(v => v.lang.includes('hi') || v.name.toLowerCase().includes('male') || v.name.toLowerCase().includes('david'));
      if (deepV) utt.voice = deepV;
      window.speechSynthesis.speak(utt);
    }

    // Tab Switcher
    function switchTab(tab) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      if (tab === 'battle') {
        event.target.classList.add('active');
        document.getElementById('battleSection').classList.remove('hidden');
        document.getElementById('advisorSection').classList.add('hidden');
      } else {
        event.target.classList.add('active');
        document.getElementById('advisorSection').classList.remove('hidden');
        document.getElementById('battleSection').classList.add('hidden');
      }
    }

    // Voice Decibel Engine
    let audioCtx, analyser, micStream;
    let isBattling = false;
    let userMaxPower = 0;
    let aiPower = 0;

    async function toggleShoutBattle() {
      const btn = document.getElementById('startShoutBtn');
      const status = document.getElementById('battleStatus');

      if (!isBattling) {
        try {
          micStream = await navigator.mediaDevices.getUserMedia({ audio: true });
          audioCtx = new (window.AudioContext || window.webkitAudioContext)();
          analyser = audioCtx.createAnalyser();
          const source = audioCtx.createMediaStreamSource(micStream);
          source.connect(analyser);
          analyser.fftSize = 256;

          isBattling = true;
          btn.innerText = "🛑 Stop & Result";
          btn.style.background = "var(--red-alert)";
          btn.style.color = "#fff";
          status.innerText = "CHILLAO! CyberPulse AI mukabla kar raha hai!";
          speakDeep("CyberPulse arena active! Chilla kar apna power dikhao!");

          trackVoiceBattle();
        } catch (err) {
          alert("Mic permission allow karein game shuru karne ke liye!");
        }
      } else {
        stopBattle();
      }
    }

    function trackVoiceBattle() {
      if (!isBattling) return;
      const dataArray = new Uint8Array(analyser.frequencyBinCount);
      analyser.getByteFrequencyData(dataArray);

      let sum = 0;
      for (let i = 0; i < dataArray.length; i++) sum += dataArray[i];
      let volume = Math.min(100, Math.floor((sum / dataArray.length) * 1.6));

      if (volume > userMaxPower) userMaxPower = volume;
      aiPower = Math.min(100, Math.floor(Math.random() * 50 + 40));

      document.getElementById('userBar').style.width = userMaxPower + "%";
      document.getElementById('userScoreText').innerText = userMaxPower + "%";
      document.getElementById('aiBar').style.width = aiPower + "%";
      document.getElementById('aiScoreText').innerText = aiPower + "%";

      requestAnimationFrame(trackVoiceBattle);
    }

    function stopBattle() {
      isBattling = false;
      if (micStream) micStream.getTracks().forEach(t => t.stop());
      if (audioCtx) audioCtx.close();

      const btn = document.getElementById('startShoutBtn');
      btn.innerText = "🎙️ Start Shouting Match";
      btn.style.background = "var(--neon-green)";
      btn.style.color = "#04170c";

      const status = document.getElementById('battleStatus');
      if (userMaxPower > aiPower) {
        status.innerText = "🔥 Winner! Tumhari aawaz me CyberPulse AI se zyada dum tha!";
        speakDeep("Shandar! Tum jeet gaye, tumhari aawaz sach me powerful thi!");
      } else {
        status.innerText = "💀 CyberPulse AI jeet gaya! Next round me zyada power lagao!";
        speakDeep("CyberPulse AI jeet gaya! Next round me thoda aur josh dikhana!");
      }
      userMaxPower = 0;
    }

    // Problem Solver Engine
    function askAI() {
      const input = document.getElementById('userInput');
      const box = document.getElementById('chatResponse');
      const val = input.value.trim().toLowerCase();
      if (!val) return;

      let ans = "";
      if (val.includes("paisa") || val.includes("earn") || val.includes("money")) {
        ans = "CyberPulse advice: Roz practical skills aur genuine traffic laane par focus karo, earning step-by-step grow hogi.";
      } else if (val.includes("tension") || val.includes("sad") || val.includes("stress")) {
        ans = "Tension lene se solutions nahi milte. Voice arena me jao aur chillane wala match khel kar mind fresh karo!";
      } else {
        ans = "CyberPulse AI ne analyze kiya: Apne targets ko daily divide karo aur regular work karte raho.";
      }
      box.innerText = ans;
      speakDeep(ans);
      input.value = "";
    }
  </script>
</body>
</html>
