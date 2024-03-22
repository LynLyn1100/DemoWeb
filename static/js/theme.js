function toggleTheme() {
    // Kiểm tra xem chủ đề hiện tại là gì
    var currentTheme = localStorage.getItem('theme');
    // Nếu chủ đề hiện tại là sáng, chuyển sang chủ đề tối và ngược lại
    if (currentTheme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'light');
      localStorage.setItem('theme', 'light');
    } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
    }
  }

   window.onload = function() {
    var currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
      document.documentElement.setAttribute('data-theme', currentTheme);
    } else {
      // Nếu chưa có chủ đề nào được lưu, mặc định là chủ đề sáng
      localStorage.setItem('theme', 'light');
    }
  }
