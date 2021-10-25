const status = document.querySelector("#status");

document.addEventListener("gamepadconnected", function (e) {
  console.log(
    "Gamepad connected at index %d: %s. %d buttons, %d axes.",
    e.gamepad.index,
    e.gamepad.id,
    e.gamepad.buttons.length,
    e.gamepad.axes.length
  );
  status.textContent = "Connected";
});

document.addEventListener("gamepaddisconnected", (e) => {
  console.log("Gamepad Disconnected");
  status.textContent = "Disconnected";
});
