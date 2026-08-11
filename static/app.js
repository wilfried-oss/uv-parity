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

    if ($("#numberInput").val() % 2 === 0) {
      result.html($("#numberInput").val() + " is even");
    } else {
      result.html($("#numberInput").val() + " is odd");
    }
  });
});
