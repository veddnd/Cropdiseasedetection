// Upload functionality
// document.querySelector('form').addEventListener('submit', function(e) {
//     e.preventDefault();
//     const fileInput = document.getElementById('plant-image');
//     if (fileInput.files.length > 0) {
//         alert('File uploaded successfully! We will now analyze the image.');
//         // You can add code here to handle the file upload and send it to the server
//     } else {
//         alert('Please select a file before submitting.');
//     }
// });

// // FAQ toggle functionality
// const faqs = document.querySelectorAll('.faq h3');
// faqs.forEach(faq => {
//     faq.addEventListener('click', function() {
//         this.parentNode.classList.toggle('open');
//     });
// });

// Upload functionality
document.querySelector('form').addEventListener('submit', function(e) {
    const fileInput = document.getElementById('plant-image');
    if (fileInput.files.length > 0) {
        alert('File uploaded successfully! We will now analyze the image.');
        // Allow the form to submit naturally
    } else {
        e.preventDefault(); // Prevent form submission if no file is selected
        alert('Please select a file before submitting.');
    }
});
