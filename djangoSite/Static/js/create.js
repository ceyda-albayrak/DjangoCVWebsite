(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()

  function fileValidation() { 
    var fileInput =  
        document.getElementById('file'); 
      
    var filePath = fileInput.value; 
  
    // Allowing file type 
    var allowedExtensions =  
            /(\.jpg|\.jpeg|\.png|\.gif)$/i; 
      
    if (!allowedExtensions.exec(filePath)) { 
        alert('Geçersiz Dosya Türü!'); 
        fileInput.value = ''; 
        return false; 
    }  
    else  
    { 
      
        // Image preview 
        if (fileInput.files && fileInput.files[0]) { 
            var reader = new FileReader(); 
            reader.onload = function(e) { 
                document.getElementById( 
                    'imagePreview').innerHTML =  
                    '<img src="' + e.target.result 
                    + '"/>'; 
            }; 
              
            reader.readAsDataURL(fileInput.files[0]); 
        } 
    } 
}

 //class adı ile uyuşan tüm nesneler

    