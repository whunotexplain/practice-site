// register.js
document.addEventListener("DOMContentLoaded", function () {
  const registerForm = document.getElementById("registerForm");
  const errorDiv = document.getElementById("error");
  const successDiv = document.getElementById("success");

  if (registerForm) {
    registerForm.addEventListener("submit", async function (event) {
      event.preventDefault();

      // Очистка сообщений
      errorDiv.textContent = "";
      successDiv.textContent = "";
      errorDiv.style.display = "none";
      successDiv.style.display = "none";

      // Получаем данные формы
      const login = document.getElementById("login").value.trim();
      const phoneNumber = document.getElementById("phone_number").value.trim();
      const password = document.getElementById("password").value;
      const passwordCheck = document.getElementById("password_check").value;

      // Валидация
      if (password !== passwordCheck) {
        showError("Пароли не совпадают");
        return;
      }

      // Подготовка данных
      const userData = {
        login: login,
        phone_number: phoneNumber,
        password: password,
      };

      try {
        // ВАЖНО: Укажите правильный URL вашего сервера
        const response = await fetch(
          "http://localhost:8080/registration/register",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(userData),
          },
        );

        const data = await response.json();

        if (response.ok) {
          showSuccess("Аккаунт успешно создан!");

          // Перенаправление через 2 секунды
          setTimeout(() => {
            window.location.href = "/pages/login";
          }, 2000);
        } else {
          showError(data.detail || "Ошибка при регистрации");
        }
      } catch (error) {
        console.error("Ошибка подключения:", error);
        showError(
          "Ошибка подключения к серверу. Проверьте, запущен ли сервер.",
        );
      }
    });
  }

  function showError(message) {
    errorDiv.textContent = message;
    errorDiv.style.display = "block";
  }

  function showSuccess(message) {
    successDiv.textContent = message;
    successDiv.style.display = "block";
  }
});
