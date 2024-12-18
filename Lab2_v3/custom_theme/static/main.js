// Функция для переключения темы
function toggleTheme() {
  document.body.classList.toggle('dark-theme');
}

// Добавляем обработчик события на кнопку переключения темы
document.addEventListener('DOMContentLoaded', () => {
  const themeToggleButton = document.getElementById('theme-toggle');
  if (themeToggleButton) {
    themeToggleButton.addEventListener('click', toggleTheme);
  }
});
