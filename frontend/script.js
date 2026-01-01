async function uploadPDF() {
  const fileInput = document.getElementById('pdfUpload');
  const uploadBtn = document.getElementById('uploadBtn');

  if (!fileInput.files.length) {
    alert("Please select a PDF first!");
    return;
  }

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  // 🔄 Loading state
  uploadBtn.disabled = true;
  uploadBtn.classList.add("loading");
  uploadBtn.textContent = "Uploading";

  try {
    const res = await fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: formData
    });

    if (!res.ok) throw new Error("Upload failed");

    // ✅ Success state
    uploadBtn.textContent = "✔ PDF Uploaded";
    uploadBtn.classList.remove("loading");
    uploadBtn.style.background = "#2e7d32"; // green
  } catch (error) {
    uploadBtn.textContent = "❌ Upload Failed";
    uploadBtn.classList.remove("loading");
    uploadBtn.style.background = "#c62828"; // red
  } finally {
    uploadBtn.disabled = false;
  }
}


async function sendMessage() {
  const input = document.getElementById('userInput');
  const chatBox = document.getElementById('chatBox');
  if (!input.value.trim()) return;

  // User message
  const userMsg = document.createElement("div");
  userMsg.className = "message user";
  userMsg.textContent = input.value;
  chatBox.appendChild(userMsg);

  const question = input.value;
  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  // Bot typing
  const botMsg = document.createElement("div");
  botMsg.className = "message bot";
  botMsg.textContent = "Typing...";
  chatBox.appendChild(botMsg);

  try {
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    botMsg.textContent = data.answer;
  } catch {
    botMsg.textContent = "Error getting response.";
  }

  chatBox.scrollTop = chatBox.scrollHeight;
}
