// Add any custom JavaScript here
console.log("Flask Todo App Loaded Successfully!");

// Optional: Add confirmation for delete actions
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('a[href^="/delete/"]');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this todo?')) {
                e.preventDefault();
            }
        });
    });
});
