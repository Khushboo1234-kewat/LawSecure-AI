// Register Form Validation
document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.querySelector("form");

  if (registerForm && window.location.pathname.includes("register.html")) {
    registerForm.addEventListener("submit", (e) => {
      const password = document.getElementById("password").value.trim();
      const confirmPassword = document.getElementById("confirm-password").value.trim();

      if (password !== confirmPassword) {
        alert("Passwords do not match!");
        e.preventDefault(); // Prevent form submission
      } else if (password.length < 6) {
        alert("Password should be at least 6 characters long.");
        e.preventDefault();
      }
    });
  }

  // Login Form Validation
  const loginForm = document.querySelector("form");
  if (loginForm && window.location.pathname.includes("login.html")) {
    loginForm.addEventListener("submit", (e) => {
      const username = document.getElementById("username").value.trim();
      const password = document.getElementById("password").value.trim();

      if (!username || !password) {
        alert("Please fill in both username and password.");
        e.preventDefault();
      }
    });
  }
});
