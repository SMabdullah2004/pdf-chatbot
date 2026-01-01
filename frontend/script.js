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
