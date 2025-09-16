/**
 * Enhanced app.js for the ADK Multi-Agent Assistant
 */

// SSE (Server-Sent Events) handling
const sessionId = Math.random().toString().substring(10);
const sse_url = "http://" + window.location.host + "/events/" + sessionId;
const send_url = "http://" + window.location.host + "/send/" + sessionId;
let eventSource = null;
let is_audio = false;

// Get DOM elements
const messageForm = document.getElementById("messageForm");
const messageInput = document.getElementById("message");
const messagesDiv = document.getElementById("messages");
const statusDiv = document.getElementById("status");
const sendButton = document.getElementById("sendButton");
const sendText = document.getElementById("sendText");
const sendLoading = document.getElementById("sendLoading");
const typingIndicator = document.getElementById("typingIndicator");
let currentMessageId = null;
let currentMessageElement = null;

// SSE handlers
function connectSSE() {
  // Connect to SSE endpoint
  eventSource = new EventSource(sse_url + "?is_audio=" + is_audio);

  // Handle connection open
  eventSource.onopen = function () {
    console.log("SSE connection opened.");
    updateStatus("Conectado", "connected");
    sendButton.disabled = false;
    addSubmitHandler();
  };

  // Handle incoming messages
  eventSource.onmessage = function (event) {
    const message_from_server = JSON.parse(event.data);
    console.log("[AGENT TO CLIENT] ", message_from_server);

    // Check if the turn is complete
    if (message_from_server.turn_complete && message_from_server.turn_complete == true) {
      currentMessageId = null;
      currentMessageElement = null;
      hideTypingIndicator();
      showSendButton();
      return;
    }

    // Check for interrupt message
    if (message_from_server.interrupted && message_from_server.interrupted === true) {
      if (audioPlayerNode) {
        audioPlayerNode.port.postMessage({ command: "endOfAudio" });
      }
      return;
    }

    // If it's audio, play it
    if (message_from_server.mime_type == "audio/pcm" && audioPlayerNode) {
      audioPlayerNode.port.postMessage(base64ToArray(message_from_server.data));
    }

    // If it's a text, print it
    if (message_from_server.mime_type == "text/plain") {
      // Add a new message for a new turn
      if (currentMessageId == null) {
        currentMessageId = Math.random().toString(36).substring(7);
        currentMessageElement = createMessageElement("assistant", "");
        messagesDiv.appendChild(currentMessageElement);
        showTypingIndicator();
        hideSendButton();
      }

      // Add message text to the existing message element
      const messageBubble = currentMessageElement.querySelector('.message-bubble');
      messageBubble.textContent += message_from_server.data;

      // Scroll down to the bottom of the messagesDiv
      messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
  };

  // Handle connection close
  eventSource.onerror = function (event) {
    console.log("SSE connection error or closed.");
    updateStatus("Desconectado", "disconnected");
    sendButton.disabled = true;
    eventSource.close();
    setTimeout(function () {
      console.log("Reconnecting...");
      connectSSE();
    }, 5000);
  };
}

// Create a message element with proper styling
function createMessageElement(type, content) {
  const messageDiv = document.createElement("div");
  messageDiv.className = `message ${type}`;
  
  const bubbleDiv = document.createElement("div");
  bubbleDiv.className = "message-bubble";
  bubbleDiv.textContent = content;
  
  const timeDiv = document.createElement("div");
  timeDiv.className = "message-time";
  timeDiv.textContent = new Date().toLocaleTimeString();
  
  messageDiv.appendChild(bubbleDiv);
  messageDiv.appendChild(timeDiv);
  
  return messageDiv;
}

// Update connection status
function updateStatus(text, className) {
  statusDiv.textContent = text;
  statusDiv.className = `status ${className}`;
}

// Show/hide typing indicator
function showTypingIndicator() {
  typingIndicator.classList.add('show');
}

function hideTypingIndicator() {
  typingIndicator.classList.remove('show');
}

// Show/hide send button with loading state
function showSendButton() {
  sendText.style.display = 'inline';
  sendLoading.style.display = 'none';
  sendButton.disabled = false;
}

function hideSendButton() {
  sendText.style.display = 'none';
  sendLoading.style.display = 'inline-block';
  sendButton.disabled = true;
}

// Add submit handler to the form
function addSubmitHandler() {
  messageForm.onsubmit = function (e) {
    e.preventDefault();
    const message = messageInput.value.trim();
    if (message) {
      // Add user message to chat
      const userMessage = createMessageElement("user", message);
      messagesDiv.appendChild(userMessage);
      
      // Clear input and send message
      messageInput.value = "";
      sendMessage({
        mime_type: "text/plain",
        data: message,
      });
      console.log("[CLIENT TO AGENT] " + message);
      
      // Scroll to bottom
      messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
    return false;
  };
}

// Send a message to the server via HTTP POST
async function sendMessage(message) {
  try {
    const response = await fetch(send_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(message)
    });
    
    if (!response.ok) {
      console.error('Failed to send message:', response.statusText);
    }
  } catch (error) {
    console.error('Error sending message:', error);
  }
}

// Decode Base64 data to Array
function base64ToArray(base64) {
  const binaryString = window.atob(base64);
  const len = binaryString.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) {
    bytes[i] = binaryString.charCodeAt(i);
  }
  return bytes;
}

// Audio handling (simplified - no audio recording)
let audioPlayerNode = null;

// Initialize audio components (only for playback)
function initAudio() {
  // Audio Player only
  if (typeof AudioWorkletNode !== 'undefined') {
    try {
      const audioContext = new (window.AudioContext || window.webkitAudioContext)();
      audioContext.audioWorklet.addModule('/static/js/pcm-player-processor.js').then(() => {
        audioPlayerNode = new AudioWorkletNode(audioContext, 'pcm-player-processor');
        audioPlayerNode.connect(audioContext.destination);
      });
    } catch (error) {
      console.log('Audio worklet not supported:', error);
    }
  }
}

// Initialize the application
function init() {
  connectSSE();
  initAudio();
  
  // Add enter key handler for input
  messageInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      messageForm.dispatchEvent(new Event('submit'));
    }
  });
}

// Start the application when DOM is loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}