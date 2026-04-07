// Dynamic UI enhancements for Job Application Tracker

// Confirm delete action
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('button[type="submit"]');
    deleteButtons.forEach(button => {
        if (button.textContent.trim().includes('Delete')) {
            button.addEventListener('click', function(e) {
                const confirmed = confirm('Are you sure you want to delete this job application?');
                if (!confirmed) {
                    e.preventDefault();
                }
            });
        }
    });
});

// Auto-focus on first input in forms
document.addEventListener('DOMContentLoaded', function() {
    const firstInput = document.querySelector('input[type="text"]');
    if (firstInput) {
        firstInput.focus();
    }
});

// Simple form validation
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], select[required]');
    for (let input of inputs) {
        if (!input.value.trim()) {
            alert('Please fill in all required fields.');
            input.focus();
            return false;
        }
    }
    return true;
}

// Add validation to forms
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(form)) {
                e.preventDefault();
            }
        });
    });
});

// Search and filter functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const statusFilter = document.getElementById('statusFilter');
    const tableRows = document.querySelectorAll('#jobsTable tr');

    function filterJobs() {
        const searchTerm = searchInput.value.toLowerCase();
        const statusValue = statusFilter.value;

        tableRows.forEach(row => {
            const company = row.getAttribute('data-company').toLowerCase();
            const status = row.getAttribute('data-status');

            const matchesSearch = company.includes(searchTerm);
            const matchesStatus = statusValue === '' || status === statusValue;

            if (matchesSearch && matchesStatus) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    if (searchInput && statusFilter) {
        searchInput.addEventListener('input', filterJobs);
        statusFilter.addEventListener('change', filterJobs);
    }
});