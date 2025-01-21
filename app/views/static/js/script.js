document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggle-sidebar');
    const sidebar = document.querySelector('.sidebar');

    toggleButton.addEventListener('click', () => {
        // Alternar a classe "collapsed" na sidebar
        sidebar.classList.toggle('collapsed');
    });
});