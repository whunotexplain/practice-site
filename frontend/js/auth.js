// Замените код в auth.js:
document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("loginForm");

  if (loginForm) {
    loginForm.addEventListener("submit", async function (e) {
      e.preventDefault();

      const login = document.getElementById("login").value;
      const password = document.getElementById("password").value;

      document.getElementById("error").style.display = "none";
      document.getElementById("success").style.display = "none";

      if (!login || !password) {
        showError("Заполните все поля!");
        return;
      }

      try {
        const authString = btoa(`${login}:${password}`);

        // ИСПРАВЛЕННЫЙ ПУТЬ - БЕЗ /api/
        const response = await fetch("/demo-auth/login/", {
          method: "POST",
          headers: {
            Authorization: `Basic ${authString}`,
            "Content-Type": "application/json",
          },
        });

        if (response.ok) {
          const data = await response.json();
          showSuccess("Успешный вход! Перенаправление...");

          setTimeout(() => {
            if (data.redirect_to) {
              window.location.href = data.redirect_to;
            } else if (data.user && data.user.role) {
              window.location.href = `/pages/${data.user.role}/dashboard`;
            } else {
              window.location.href = "/";
            }
          }, 1000);
        } else {
          if (response.status === 401) {
            showError("Неверный логин или пароль!");
          } else {
            showError(`Ошибка сервера: ${response.status}`);
          }
        }
      } catch (error) {
        showError("Ошибка соединения с сервером");
        console.error(error);
      }
    });
  }

  function showError(message) {
    const errorDiv = document.getElementById("error");
    if (errorDiv) {
      errorDiv.textContent = message;
      errorDiv.style.display = "block";
    }
  }

  function showSuccess(message) {
    const successDiv = document.getElementById("success");
    if (successDiv) {
      successDiv.textContent = message;
      successDiv.style.display = "block";
    }
  }
});
