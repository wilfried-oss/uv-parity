$(function () {
  const result = $("#result");
  const checkBtn = $("#checkBtn");

  $("#numberInput").on("focus", function () {
    result.html("");
  });

  $("#numberInput").on("input", function () {
    let value = $(this).val();
    if (!/[0-9]/.test(value)) {
      value = value.substring(0, value.length - 1);
    }
    $(this).val(value);
  });

  $("form").on("submit", function (e) {
    e.preventDefault();
    if (!$("#numberInput").val()) {
      result.append("NO GIVEN NUMBER");
      return;
    }

    let number = $("#numberInput").val();

    $.ajax({
      url: "/check_parity",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify({ number: parseInt(number) }),
      success: function (response) {
        $("#result").text(`${response.number} is ${response.parity}`);
      },
      error: function (xhr) {
        $("#result").text("Erreur : " + xhr.responseText);
      },
    });
  });
});
