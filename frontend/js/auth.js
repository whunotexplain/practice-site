document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("loginForm");

  if (loginForm) {
    loginForm.addEventListener("submit", async function (e) {
      e.preventDefault();

      const login = document.getElementById("login").value.trim();
      const password = document.getElementById("password").value;

      document.getElementById("error").style.display = "none";
      document.getElementById("success").style.display = "none";

      if (!login || !password) {
        showError("Заполните все поля!");
        return;
      }

      try {
        const authString = btoa(`${login}:${password}`);

        const response = await fetch("/demo-auth/login/", {
          method: "POST",
          headers: {
            Authorization: `Basic ${authString}`,
            "Content-Type": "application/json",
          },
        });

        console.log("URL запроса:", "/demo-auth/login/");
        console.log("Статус ответа:", response.status);

        if (response.ok) {
          const data = await response.json();
          console.log("Данные ответа:", data);

          showSuccess("Успешный вход!");

          if (data.status === "success" && data.user && data.user.role) {
            setTimeout(() => {
              if (data.redirect_to) {
                window.location.href = data.redirect_to;
              } else {
                window.location.href = `/pages/${data.user.role}/dashboard`;
              }
            }, 1000);
          } else {
            showError("Ошибка: сервер не подтвердил авторизацию");
          }
        } else {
          if (response.status === 401) {
            showError("Неверный логин или пароль!");
          } else {
            const errorText = await response.text();
            showError(`Ошибка сервера: ${response.status}`);
            console.error("Текст ошибки:", errorText);
          }
        }
      } catch (error) {
        showError("Ошибка соединения с сервером");
        console.error("Ошибка fetch:", error);
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
