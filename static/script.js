function handleFile() {
  const fileInput = document.getElementById("file-input")
  fileInput.click();
}


document.getElementById('submit-btn').addEventListener('click', () => {
  const fileInput = document.getElementById("file-input")
  const fileSubmit = document.getElementById("file-submit")
  if (fileInput.files.length > 0) {
    console.log('File name: ', fileInput.files[0].name);
    fileSubmit.click();
    fetch('/processingFile')
    .then()
  }
});


document.querySelectorAll('.stop-btn').forEach(button => {
  button.addEventListener('click', () => {
    alert('Stop functionality to be implemented!');
  });
});


// document.querySelectorAll('.download-btn').forEach(button => {
//   button.addEventListener('click', () => {
//     alert('Download functionality to be implemented!');
//   });
// });
