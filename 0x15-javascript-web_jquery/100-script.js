document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  header.addEventListener('click', function () {
    header.style.color = 'red';
  });
});
