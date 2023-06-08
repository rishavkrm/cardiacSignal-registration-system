function handleUpload() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) {
      console.error('No file selected');
      return;
    }
    const formData = new FormData();
    formData.append('file', file);
    console.log(formData)
    fetch('http://127.0.0.1:9000/api/v1/classifier', {
      method: 'POST',
      body: formData,
    })
      .then(response => {return response.json()})
      .then(data => {
        const processedDataElement = document.getElementById('processedData');
        processedDataElement.innerHTML = `Uploaded file is `+data.result;
        
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
  const btn = document.querySelector(".button");
        const btnText = document.querySelector("#btnText");

        btn.onclick = () => {
            handleUpload()

        };